#!/usr/bin/env python3
"""
Decoder for the custom “rot‑LCG‑Base64” encoder.

Usage:
    python decoder.py <encoded_string>

The script mirrors the steps performed in `encode_flag` but in reverse:

1. URL‑safe Base64‑decode (adding back any stripped padding).
2. Extract the 2‑byte little‑endian length header.
3. Re‑generate the identical LCG keystream from that length.
4. XOR the ciphertext with the keystream.
5. Undo the per‑byte left‑rotation (right‑rotate by the same amount).
6. Reverse the byte order.
7. Decode the resulting bytes as UTF‑8 → original flag.
"""

import sys
import base64


def rotr8(x: int, r: int) -> int:
    """Circular right‑rotate of an 8‑bit value."""
    return ((x >> r) & 0xFF) | ((x << (8 - r)) & 0xFF)


def lcg_stream(seed: int, n: int):
    """Re‑create the same pseudo‑random byte stream used during encoding."""
    a = 1664525
    c = 1013904223
    m = 2 ** 32
    s = seed & 0xFFFFFFFF
    out = []
    for _ in range(n):
        s = (a * s + c) % m
        out.append((s >> 16) & 0xFF)   # high byte of the state
    return out


def decode_flag(encoded: str) -> str:
    """
    Decode a string produced by `encode_flag`.
    Returns the original UTF‑8 flag (or raises if something goes wrong).
    """

    # ------------------------------------------------------------------
    # 1️⃣ Base64‑decode (URL‑safe, padding may have been stripped)
    # ------------------------------------------------------------------
    # Pad the string to a multiple of 4 characters, as required by b64.
    pad_len = (-len(encoded)) % 4
    encoded_padded = encoded + ("=" * pad_len)
    payload = base64.urlsafe_b64decode(encoded_padded)

    # ------------------------------------------------------------------
    # 2️⃣ Pull out the 2‑byte little‑endian length header
    # ------------------------------------------------------------------
    if len(payload) < 2:
        raise ValueError("Payload too short – missing length header.")
    L = payload[0] | (payload[1] << 8)   # reconstruct original length
    ciphertext = payload[2:]            # the actual encrypted bytes

    if len(ciphertext) != L:
        # The encoder always produces exactly L ciphertext bytes,
        # but we keep a sanity check in case the input is malformed.
        raise ValueError(
            f"Length mismatch: header says {L} bytes, "
            f"but payload contains {len(ciphertext)} bytes."
        )

    # ------------------------------------------------------------------
    # 3️⃣ Regenerate the keystream using the same seed derivation
    # ------------------------------------------------------------------
    seed = (L * 0x9E3779B1) & 0xFFFFFFFF
    keystream = lcg_stream(seed, L)

    # ------------------------------------------------------------------
    # 4️⃣ XOR ciphertext with keystream → rotated plaintext
    # ------------------------------------------------------------------
    rotated = bytes(c ^ k for c, k in zip(ciphertext, keystream))

    # ------------------------------------------------------------------
    # 5️⃣ Undo the per‑byte left rotation (right‑rotate by same amount)
    # ------------------------------------------------------------------
    unrotated = bytes(
        rotr8(byte, (i % 7) + 1)   # rotation amount repeats every 7 bytes
        for i, byte in enumerate(rotated)
    )

    # ------------------------------------------------------------------
    # 6️⃣ Reverse the byte order back to original
    # ------------------------------------------------------------------
    original_bytes = unrotated[::-1]

    # ------------------------------------------------------------------
    # 7️⃣ Decode UTF‑8 → human readable flag
    # ------------------------------------------------------------------
    try:
        return original_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(
            "Decoded bytes are not valid UTF‑8. The input may be corrupted."
        ) from exc


# ----------------------------------------------------------------------
# CLI entry point
# ----------------------------------------------------------------------
if __name__ == "__main__":
    # Accept the encoded string either as a command‑line argument
    # or from stdin (useful for piping).
    if len(sys.argv) >= 2:
        encoded_input = sys.argv[1].strip()
    else:
        encoded_input = sys.stdin.read().strip()

    if not encoded_input:
        sys.exit("Usage: python decode_flag.py <base64_string>")

    try:
        flag = decode_flag(encoded_input)
        print(flag)
    except Exception as e:
        sys.exit(f"[!] Decoding failed: {e}")
