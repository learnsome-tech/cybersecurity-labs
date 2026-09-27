# Exercises — Asymmetric Cryptography: RSA, ECC & Diffie-Hellman

Lesson `m03l02` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l02)

## Exercise 1: Swap the keys and predict

1. dh_modp.py: change Bob's private value. Predict which output lines change, then run it.
2. ecdh.sh: add a third pair, mallory, derive with bob.pub. Does it match alice.bin?
3. sign.sh: verify rsa.sig against ed.pub instead of rsa.pub. Predict the result first.
4. sign.sh: set rsa_keygen_bits to 2048. Which sizes change, and to what?

> **Hint**: An RSA signature is as long as the modulus: 2048 bits is 256 bytes. A derived secret depends on both private keys involved.


---

© LearnSome.tech · support@iwantto.learnsome.tech
