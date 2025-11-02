import sys
import base64

def rotl8(x, r):
    return ((x << r) & 0xFF) | (x >> (8 - r))

def lcg_stream(seed, n):
    a = 1664525
    c = 1013904223
    m = 2**32
    s = seed & 0xFFFFFFFF
    out = []
    for _ in range(n):
        s = (a * s + c) % m
        out.append((s >> 16) & 0xFF)   
    return out

def encode_flag(flag: str) -> str:
    b = flag.encode('utf-8')
    L = len(b)

    rev = b[::-1]

    rotated = bytes(rotl8(byte, (i % 7) + 1) for i, byte in enumerate(rev))

    seed = (L * 0x9E3779B1) & 0xFFFFFFFF  
    ks = lcg_stream(seed, len(rotated))

    xored = bytes(b ^ k for b, k in zip(rotated, ks))

    header = bytes([L & 0xFF, (L >> 8) & 0xFF])
    payload = header + xored

    enc = base64.urlsafe_b64encode(payload).decode('ascii').rstrip('=')
    return enc

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        flag = sys.argv[1]
    else:
        flag = input("Enter flag to encode: ").strip()
    print(encode_flag(flag))
