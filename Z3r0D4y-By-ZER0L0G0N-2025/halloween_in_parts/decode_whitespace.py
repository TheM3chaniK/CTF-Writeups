#!/usr/bin/env python3
from pathlib import Path

# === 1️⃣ Load data ===
fname = "Halloween.txt"
data = Path(fname).read_bytes()

marker = b'Part1:"zero{4_'  # adjust if different
start = data.find(marker)
if start == -1:
    raise SystemExit("Marker not found")

tail = data[start + len(marker):]

# === 2️⃣ Keep only spaces and tabs ===
tail = bytes([c for c in tail if c in (9, 32)])
print(f"Length of whitespace section: {len(tail)}")

# === 3️⃣ Convert spaces/tabs → bits ===


def bits_from_tail(tail, space_is_zero=True):
    return "".join(
        "0" if (c == 32 and space_is_zero) or (c == 9 and not space_is_zero)
        else "1"
        for c in tail
    )


def bytes_from_bits(bits):
    out = bytearray()
    for i in range(0, len(bits) - 7, 8):
        out.append(int(bits[i: i + 8], 2))
    return bytes(out)


bits = bits_from_tail(tail, space_is_zero=True)
decoded = bytes_from_bits(bits)

# === 4️⃣ Save result ===
outf = "decoded.bin"
Path(outf).write_bytes(decoded)
print(f"Saved decoded data to {outf} ({len(decoded)} bytes)")

# === 5️⃣ Detect possible file type ===
magic = decoded[:8]
if magic.startswith(b"\x89PNG"):
    ext = ".png"
elif magic.startswith(b"\xff\xd8\xff"):
    ext = ".jpg"
elif magic.startswith(b"PK\x03\x04"):
    ext = ".zip"
else:
    ext = ".bin"

Path(f"decoded{ext}").write_bytes(decoded)
print(f"Possible output file: decoded{ext}")
