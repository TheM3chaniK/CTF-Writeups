import urllib.parse

flag = "###REDACTED###"
encoded = ""

for ch in flag:
    ascii_val = ord(ch)
    transformed = (ascii_val + 10) * 16
    encoded += urllib.parse.quote(str(transformed))

print(encoded)
