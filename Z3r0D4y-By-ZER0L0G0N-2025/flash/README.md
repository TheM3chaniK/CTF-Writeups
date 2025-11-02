# 🧩 Challenge: Flash

**Category:** Forensics
**Points:** 100

---

### 🔖 **Challenge Description**

Courage the Cowardly Dog flashed something… (the flag, of course 👀). Are you quick enough?

---

### 📎 **Attachments**

> [flash.gif](./flash.gif)

---

### 🧭 **Initial Observations**

* Looking at the GIF, I could immediately tell that the flag flashes for just a split second — classic “blink and you miss it” move.
  Courage would probably scream and run to Muriel shouting, *“THE FLAG! IT’S HAUNTED!!”* while we just calmly open our terminal. 🧠💻

---

### 🛠 **Environment & Tools**

* OS: I use Arch Btw
* Tools: ffmpeg
* Assumptions: Extract all frames from the GIF and find the one where Courage’s nightmare (aka the flag) appeared.

---

### ⚙️ **Artifact Recovery & Decoding Steps**

Using ffmpeg, I extracted all frames:

```bash
$ mkdir frames
$ ffmpeg -i flash.gif frames/frame_%04d.png
```

Now, let’s find which frame holds the secret.
After going through the frames (feeling like Courage running through spooky corridors), one frame flashed the flag clear as day — the same way Courage’s eyes pop out when something scary happens.

And there it was:

**`zero{gif_to_frames}`**

The flag was literally staring at me. Courage would’ve fainted. 💀

---

### 🔁 **Recovered Artifacts / Outputs**

* Extracted frames from `flash.gif`
* Frame showing the hidden flag

---

### ✅ **Validation**

* The flag is *visibly* present in one of the extracted frames.
* It follows the usual `zero{}` flag format used throughout the CTF.
* Verified by viewing the same frame again (and laughing at Courage for missing it).

---

### 🏁 **Flag**

```
zero{gif_to_frames}
```

---

### 💡 **Takeaways**

* If something flashes on screen, don’t blink — Courage would, but you shouldn’t.
* ffmpeg is the Swiss Army knife of digital forensics. Use it, don’t fear it.
* Sometimes the flag isn’t hidden in code, but right before your terrified eyes.
* Always check every frame — even if you look like you’re in a horror movie montage doing it. 🎬
* Courage may be scared, but true hackers fear nothing — except maybe `Segmentation fault (core dumped)`.

---

**Solved by TheM3chanik — [contact@them3chanik.com](mailto:contact@them3chanik.com)**

---
