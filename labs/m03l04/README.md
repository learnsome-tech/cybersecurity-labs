# m03l04 · Public Key Infrastructure: X.509 Certificates & CAs

Module 3: Applied Cryptography & Keys · lesson 3.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m03l04)

**Goal:** You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m03l04-02](m03l04-02/) | Build a CA, request a certificate, issue it | Graded |
| [m03l04-03](m03l04-03/) | Four checks a client makes | Graded |
| [m03l04-05](m03l04-05/) | Revoking a certificate with a CRL | Graded |
| [m03l04-06](m03l04-06/) | OCSP: one question, one signed answer | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the CA

1. mkpki.sh: add DNS:shop.example.com to the request. Predict the wrong-name check, then rerun.
2. verify.sh: set JAN_1=1795000000, mid-November 2026. Which result changes, and why?
3. Put an intermediate CA between root and leaf; pass it to openssl verify with -untrusted.
4. ocsp.sh: delete the revoke step. What status does the responder give now?

> **Hint:** An intermediate needs basicConstraints CA:TRUE and must be signed by the root. A serial the CA has no record of is not good.

## Check yourself

- In verify.sh the impostor certificate had the right name and a valid signature, yet it failed. What was missing?
- The certificate for www.example.com failed for shop.example.com. Which field decided that, and how would you fix it?
- Without the CRL, openssl verify accepted a certificate whose key had leaked. What does that say about clients that skip revocation checks?
- Why does OCSP stapling protect a user's privacy better than the browser asking the CA's OCSP responder directly?
- Why does a root CA keep its private key offline and issue through intermediates?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
