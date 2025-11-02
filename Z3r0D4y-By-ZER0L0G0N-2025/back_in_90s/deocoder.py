with open("./chall.txt", "r") as f:
    data = f.read()

for line in data.splitlines():
    print("".join("█" if c == "1" else " " for c in line))
