# Exercises — Public Key Infrastructure: X.509 Certificates & CAs

Lesson `m03l04` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m03l04)

## Exercise 1: Extend the CA

1. mkpki.sh: add DNS:shop.example.com to the request. Predict the wrong-name check, then rerun.
2. verify.sh: set JAN_1=1795000000, mid-November 2026. Which result changes, and why?
3. Put an intermediate CA between root and leaf; pass it to openssl verify with -untrusted.
4. ocsp.sh: delete the revoke step. What status does the responder give now?

> **Hint**: An intermediate needs basicConstraints CA:TRUE and must be signed by the root. A serial the CA has no record of is not good.


---

© LearnSome.tech · support@iwantto.learnsome.tech
