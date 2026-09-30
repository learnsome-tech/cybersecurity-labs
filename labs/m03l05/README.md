# m03l05 · Post-Quantum Cryptography & Key Lifecycles

Module 3: Applied Cryptography & Keys · lesson 3.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m03l05)

**Goal:** You can explain what a quantum computer would break, run ML-KEM and ML-DSA and weigh their sizes, plan a hybrid migration, and rotate keys with envelope encryption.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l05-02](m03l05-02/) | ML-KEM: key exchange built to survive Shor | Runs, not graded |
| [m03l05-03](m03l05-03/) | Post-quantum signatures and what they weigh | Runs, not graded |
| [m03l05-06](m03l05-06/) | Envelope encryption: rotate without re-encrypting | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Measure the cost, then rotate

1. mlkem.sh: switch to ML-KEM-1024. Predict which of the three sizes change, then run it.
2. pqsign.sh: add ML-DSA-87 and SLH-DSA-SHA2-128f to the loop. Which grows, key or signature?
3. envelope.py: after rotation, open the new wrap with kek_v1. What happens, and why?
4. envelope.py: rotate the DEK instead of the KEK. What must now happen to the row?

> **Hint:** ML-KEM secrets are always 32 bytes. Rotating a DEK means decrypting and re-encrypting everything it protects.

## Check yourself

- Why does harvest now, decrypt later push key exchange to post-quantum algorithms before a quantum computer exists, while signatures can follow later?
- Why does AES-256 survive the quantum threat when RSA-3072 does not?
- mlkem.sh printed a 1206-byte public key and a 1088-byte ciphertext. What does that cost a TLS handshake, and why do deployments run it as a hybrid with X25519?
- In envelope.py the stored row never changed during rotation. Why, and what would rotating the DEK require instead?
- An auditor finds the production database encryption key in a config file in Git. Which lifecycle stages have failed, and what should replace the file?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
