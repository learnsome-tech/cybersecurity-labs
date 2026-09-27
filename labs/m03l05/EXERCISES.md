# Exercises — Post-Quantum Cryptography & Key Lifecycles

Lesson `m03l05` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l05)

## Exercise 1: Measure the cost, then rotate

1. mlkem.sh: switch to ML-KEM-1024. Predict which of the three sizes change, then run it.
2. pqsign.sh: add ML-DSA-87 and SLH-DSA-SHA2-128f to the loop. Which grows, key or signature?
3. envelope.py: after rotation, open the new wrap with kek_v1. What happens, and why?
4. envelope.py: rotate the DEK instead of the KEK. What must now happen to the row?

> **Hint**: ML-KEM secrets are always 32 bytes. Rotating a DEK means decrypting and re-encrypting everything it protects.


---

© LearnSome.tech · support@iwantto.learnsome.tech
