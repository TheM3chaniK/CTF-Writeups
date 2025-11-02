#!/usr/bin/env python3
"""
decode_qr_b64_pyzbar.py
Uses only pyzbar + Pillow to decode QR codes in images in the current directory,
extract base64-like substrings from the QR payload(s), decode them and write
results line-by-line to decoded_messages.txt

Output format (one per line):
<filename>\t<decoded-text>     (newlines in decoded text are escaped as \n)
or
<filename>\tHEX:<hexbytes>     (if decoded bytes are not valid UTF-8)
or
<filename>\tRAW:<payload>      (if no base64 candidate found)
or
<filename>\tB64FAIL:<candidate> (if candidate looked like base64 but failed decode)
"""

import re
import base64
from pathlib import Path
from pyzbar.pyzbar import decode as zbar_decode
from PIL import Image

# base64-like regex (bytes form). Match sequences >= 8 chars with optional padding
B64_RE = re.compile(rb"([A-Za-z0-9_\-+/]{8,}={0,2})")

# image extensions to consider
IMG_EXTS = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff", ".webp"}


def find_image_files(directory: Path):
    return sorted(
        p for p in directory.iterdir() if p.suffix.lower() in IMG_EXTS and p.is_file()
    )


def decode_qr_with_pyzbar(path: Path):
    """Return list of decoded QR payload strings (utf-8) from image at path."""
    try:
        img = Image.open(path)
    except Exception:
        return []
    out = []
    try:
        objs = zbar_decode(img)
        for o in objs:
            # decode as utf-8, replace invalid with U+FFFD
            s = o.data.decode("utf-8", errors="replace")
            out.append(s)
    except Exception:
        pass
    return out


def extract_b64_candidates(payload: str):
    """Return list of bytes objects (candidates) that look like base64 within payload."""
    bs = payload.encode("utf-8", errors="ignore")
    # remove whitespace/newlines that may break regex
    bs = re.sub(rb"\s+", b"", bs)
    return [m.group(1) for m in B64_RE.finditer(bs)]


def try_b64_decode(candidate: bytes):
    """Try standard and URL-safe base64 decode; fix padding as needed.
    Return decoded bytes or None on failure."""
    # Fix padding
    pad = (-len(candidate)) % 4
    if pad:
        candidate = candidate + (b"=" * pad)
    # Try standard then urlsafe
    for fn in (base64.b64decode, base64.urlsafe_b64decode):
        try:
            return fn(candidate)
        except Exception:
            continue
    return None


def collapse_newlines_text(s: str):
    return s.replace("\r", "").replace("\n", "\\n")


def main():
    cwd = Path(".").resolve()
    imgs = find_image_files(cwd)
    if not imgs:
        print("No image files found in current directory.")
        return

    out_lines = []

    for img_path in imgs:
        payloads = decode_qr_with_pyzbar(img_path)
        if not payloads:
            out_lines.append(f"{img_path.name}\tRAW:<no-qr-found>")
            continue

        for payload in payloads:
            candidates = extract_b64_candidates(payload)
            if not candidates:
                # if entire payload is long, try whole string as candidate
                raw_bytes = payload.encode("utf-8", errors="ignore")
                if len(raw_bytes) >= 8:
                    candidates = [raw_bytes]

            if not candidates:
                # nothing that looks like base64; store raw payload
                # escape internal newlines
                out_lines.append(
                    f"{img_path.name}\tRAW:{
                        collapse_newlines_text(payload)}"
                )
                continue

            for cand in candidates:
                dec = try_b64_decode(cand)
                if dec is None:
                    try:
                        # candidate printable? show it
                        out_lines.append(
                            f"{img_path.name}\tB64FAIL:{
                                cand.decode('utf-8', errors='ignore')}"
                        )
                    except:
                        out_lines.append(f"{img_path.name}\tB64FAIL:{cand!r}")
                    continue

                # If decoded bytes are valid UTF-8 -> store text (escape newlines)
                try:
                    text = dec.decode("utf-8")
                    out_lines.append(
                        f"{img_path.name}\t{
                            collapse_newlines_text(text)}"
                    )
                except Exception:
                    # store hex if not text
                    out_lines.append(f"{img_path.name}\tHEX:{dec.hex()}")

    # write results (one decoded entry per line)
    out_file = cwd / "decoded_messages.txt"
    with out_file.open("w", encoding="utf-8") as f:
        for line in out_lines:
            f.write(line + "\n")

    print(f"Done. Wrote {len(out_lines)} lines to {out_file}")


if __name__ == "__main__":
    main()
