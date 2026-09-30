# m03l01-04 · ChaCha20-Poly1305 and a reused nonce

**Lesson:** [Symmetric Encryption: AES-GCM & ChaCha20](https://learnsome.tech/learn/cybersecurity-course/m03l01) (lesson 3.1, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can explain what AES-GCM and ChaCha20-Poly1305 add to a plain cipher, show a bit-flip attack failing against a tag, and spot the nonce reuse that breaks both.

In the lesson: ChaCha twenty Poly thirteen oh five is the other authenticated cipher in T L S one point three. It is fast in plain software, which is why phones and small devices without A E S hardware favour it. Same seal and open interface. The bug here is a common one: the nonce is a constant, so two messages go out under one key and one nonce. That means both were combined with identical keystream. The attacker already knows the first message, a routine status line. Exclusive-or that plaintext with its ciphertext and you have the keystream, which unlocks the second message. Run it. The door code comes back without the key, and message two still opens cleanly, because a tag only proves nobody edited the bytes. With A E S G C M the damage goes further: a repeated nonce also leaks the value used to compute tags, so forgeries follow.

## Files

- [`starter/aead.py`](starter/aead.py)
- [`starter/nonce_reuse.py`](starter/nonce_reuse.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l01/m03l01-04/starter`
2. Read `nonce_reuse.py` the way the lesson builds it:
   - Lines 1–5: same seal and open interface
   - Lines 6–11: two messages go out under one key
   - Lines 12–17: which unlocks the second message
3. Run it: `python3 nonce_reuse.py`.
4. Check it from the repository root: `./check m03l01-04`.

## Expected output

```text
message two still opens: new door code is 7713, change Friday
recovered without the key: new door code is 7713, change Friday
```

## How to check

`./check m03l01-04` copies `starter/` into a scratch directory and runs `python3 nonce_reuse.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
