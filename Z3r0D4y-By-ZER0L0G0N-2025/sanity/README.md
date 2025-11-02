# 🧩 Challenge: Sanity

**Category:** General
**Points:** 50

---

### 🔖 Challenge Description

> The flag is hidden somewhere in our discord server
>
> [https://discord.gg/3mwQ9kQdx8](https://discord.gg/3mwQ9kQdx8)

---

### 🧭 Initial Reconnaissance (aka "I clicked things")

* **Step 1 — Join the server:** Open the invite and join the Zero Logon Discord.
* **Step 2 — Inspect channels & pins:** Don’t spam — actually read channel names and check pinned messages.
* **Step 3 — Copy the payload:** Found this suspicious blob in the pinned message:

  ```
  emVyb3t0aGlzX2lzX2FfZmxhZ30
  ```

---

### 🔍 Analysis & Enumeration (a.k.a. "this smells like Base64")

* **Observation:** The token’s charset and structure scream Base64. It’s the CTF equivalent of 'please decode me'.
* **Hypothesis:** Decoding with Base64 will reveal the flag.
* **Tools:** Terminal `echo` + `base64` — minimal dependencies, maximal swagger.

---

### ⚙️ Exploitation Process (the single-command flex)

1. **Approach:** Treat the string as Base64 and decode. If it’s garbled, pivot (but it wasn’t).
2. **Execution:** One terminal command to rule them all.
3. **Confirmation:** Output is a perfectly formatted flag — no weird symbols, no crying.

```bash
# decode like it’s 1999 and also 2025
echo "emVyb3t0aGlzX2lzX2FfZmxhZ30" | base64 -d
# -> zero{this_is_a_flag}
```

---

### 💻 Code / Script Used

```bash
echo "emVyb3t0aGlzX2lzX2FfZmxhZ30" | base64 -d
```

---

### 🏁 Flag

```
zero{this_is_a_flag}
```

---

### 💡 Takeaways (aka brain-dumps & humblebrags)

* Pinned messages are tiny, sticky treasure chests — always check pins.
* Base64 is the "under-the-door-mat" of CTFs. Try it first, and then feel very clever when it works.
* Sanity checks = fast dopamine. Collect them greedily.

---

**Solved by TheM3chanik — [contact@them3chanik.com](mailto:contact@them3chanik.com)**

