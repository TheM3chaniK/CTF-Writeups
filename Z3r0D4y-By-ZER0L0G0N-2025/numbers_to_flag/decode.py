# decode.py (conceptual)
s = input().strip()
i = 0
out = []
while i < len(s):
    # try 4 digits then 3 digits (the encoder produces values like 1712, 720, ...)
    for l in (4, 3, 2):
        if i + l > len(s):
            continue
        part = s[i : i + l]
        v = int(part)
        if v % 16 != 0:
            continue
        ch_code = v // 16 - 10
        if 32 <= ch_code <= 126:  # printable
            out.append(chr(ch_code))
            i += l
            break
    else:
        # fallback if nothing matched
        i += 1
print("".join(out))
