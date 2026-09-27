# Exercises — Symmetric Encryption: AES-GCM & ChaCha20

Lesson `m03l01` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l01)

## Exercise 1: Tamper, predict, run

1. gcm_tamper.py: open with header invoice 2026-0043 instead. Predict the result, then run it.
2. Switch both calls to ChaCha20-Poly1305. Does the ciphertext still match the CTR program?
3. nonce_reuse.py: give the second message its own nonce, bytes(11) + b'\x01', and rerun.
4. Set KEY = secrets.token_bytes(32). Why does the ciphertext now change on every run?

> **Hint**: The tag covers the header, the nonce and every ciphertext byte. The counter mode match is an AES fact, not a GCM one.


---

© LearnSome.tech · support@iwantto.learnsome.tech
