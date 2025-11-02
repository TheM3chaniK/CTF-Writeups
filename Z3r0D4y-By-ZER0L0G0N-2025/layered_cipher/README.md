# 🧩 Challenge: Layered Cipher

**Category:** Crypto

**Points:** 100

---

### 🔖 Challenge Description

> A mysterious engineer left behind a Python script that transforms a secret flag into a strange sequence of characters.

### 📎 Attachments

> [chall.txt](./chall.txt)

> [CrypEncode.py](./CrypEncode.py)

---

### 🧩 First Impressions

🧐 So we got two files — looking at the Python script and the text file, it’s clear that `CrypEncode.py` is the **encoder** of `chall.txt`.
That means my job is simple (but tricky): build the **decoder** that undoes every step. 🔄

---

### 🧮 Breaking It Down

Let’s see what the script does step by step:

```text
1. Takes an input string flag.
2. Converts it to UTF-8 bytes.
3. Reverses the byte order.
4. Rotates each byte left by a small, position-dependent amount.
5. Generates a pseudorandom keystream from a linear congruential generator (LCG) seeded from the flag length, and XORs the rotated bytes with that keystream.
6. Prepends a 2-byte header containing the flag length (little-endian).
7. Base64 URL-safe encodes the header+XORed payload and strips = padding.
8. Prints that string.
```

🧩 So basically, it’s an **LCG + rotation + XOR combo** — all packed behind a Base64 layer.
Now I just need to reverse these steps one by one. 🔁

---

### 🧠 Final Decoding

💻 I made a custom [decoder](./crypto_decrypt.py) that reverses each encoding stage exactly.

```bash
$ cat chall.txt | python3 crypto_decrypt.py
zero{r3v3rs3d_and_x0red}
```

🥳 And hurrah! We got the flag.

---

### 🏁 Flag

```
zero{r3v3rs3d_and_x0red}
```

---

### 💡 Takeaways

* Don’t panic when you see layered ciphers — just **trace the transformations backward** 🧩
* You don’t always have to “guess” the decryption; sometimes, **reverse-engineering the logic** is the cleanest way 🧠

---

**Solved by TheM3chanik — [contact@them3chanik.com](mailto:contact@them3chanik.com)**

---

