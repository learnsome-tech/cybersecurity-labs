# m03l02 · Asymmetric Cryptography: RSA, ECC & Diffie-Hellman

Module 3: Applied Cryptography & Keys · lesson 3.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m03l02)

**Goal:** You can show two parties agreeing a key in public with Diffie-Hellman and X25519, compare RSA and elliptic curve key and signature sizes, and explain why authentication and forward secrecy still matter.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l02-02](m03l02-02/) | Diffie-Hellman in a real 2048-bit group | Graded |
| [m03l02-03](m03l02-03/) | The same idea on an elliptic curve: X25519 | Graded |
| [m03l02-04](m03l02-04/) | Signatures with RSA and Ed25519 | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Swap the keys and predict

1. dh_modp.py: change Bob's private value. Predict which output lines change, then run it.
2. ecdh.sh: add a third pair, mallory, derive with bob.pub. Does it match alice.bin?
3. sign.sh: verify rsa.sig against ed.pub instead of rsa.pub. Predict the result first.
4. sign.sh: set rsa_keygen_bits to 2048. Which sizes change, and to what?

> **Hint:** An RSA signature is as long as the modulus: 2048 bits is 256 bytes. A derived secret depends on both private keys involved.

## Check yourself

- An eavesdropper recorded both public values in the Diffie-Hellman demo. Why can they still not compute the shared secret?
- ecdh.sh printed a 44-byte public key where the Diffie-Hellman value was 256 bytes. Why does the elliptic curve get away with less?
- After sed changed one character of release.txt, both signatures failed. What did the verifier detect, and which key did it need?
- An attacker records TLS 1.2 sessions that used RSA key transport, then steals the server's private key a year later. What can they read, and how does TLS 1.3 prevent it?
- The Diffie-Hellman maths is sound, so why is an unauthenticated exchange still open to a man-in-the-middle?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
