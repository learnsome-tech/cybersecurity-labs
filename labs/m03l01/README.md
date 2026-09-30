# m03l01 · Symmetric Encryption: AES-GCM & ChaCha20

Module 3: Applied Cryptography & Keys · lesson 3.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m03l01)

**Goal:** You can explain what AES-GCM and ChaCha20-Poly1305 add to a plain cipher, show a bit-flip attack failing against a tag, and spot the nonce reuse that breaks both.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l01-02](m03l01-02/) | Counter mode hides the amount but not the edit | Graded |
| [m03l01-03](m03l01-03/) | AES-GCM refuses the same edit | Graded |
| [m03l01-04](m03l01-04/) | ChaCha20-Poly1305 and a reused nonce | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tamper, predict, run

1. gcm_tamper.py: open with header invoice 2026-0043 instead. Predict the result, then run it.
2. Switch both calls to ChaCha20-Poly1305. Does the ciphertext still match the CTR program?
3. nonce_reuse.py: give the second message its own nonce, bytes(11) + b'\x01', and rerun.
4. Set KEY = secrets.token_bytes(32). Why does the ciphertext now change on every run?

> **Hint:** The tag covers the header, the nonce and every ciphertext byte. The counter mode match is an AES fact, not a GCM one.

## Check yourself

- In the counter mode program, why could the attacker change the amount without knowing the key?
- The AES-GCM ciphertext matched the AES-CTR ciphertext byte for byte. So what does GCM add, and when does it act?
- Two messages were sealed with ChaCha20-Poly1305 under the same key and nonce, and both tags verified. What did the attacker need to read the second message?
- A service picks random 96-bit nonces for AES-GCM and has used one key for years at very high volume. What is the risk, and what is the fix?
- A vendor says its data masking 'encrypts' customer card numbers. Why is that claim wrong?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
