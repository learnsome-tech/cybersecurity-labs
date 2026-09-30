# m03l04-06 · OCSP: one question, one signed answer

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Read along

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: The online certificate status protocol, O C S P, asks about one certificate instead of downloading a whole list. It normally runs over H T T P; here the request and response are files, so each step is visible without a network. The same revocation is recorded first. The client builds a request naming the issuer and the serial number. The responder looks the serial up in the C A database and signs an answer. Then the client checks the responder's signature and reads the status. Run it. Response verify O K, then revoked, reason key compromise. Plain O C S P has two problems: every lookup tells the responder which site you are visiting, and when the responder is down, browsers usually carry on anyway. O C S P stapling fixes the first: the server fetches this signed response itself and sends it inside the T L S handshake.

## Files

- [`starter/ca.cnf`](starter/ca.cnf)
- [`starter/command.txt`](starter/command.txt)
- [`starter/mkpki.sh`](starter/mkpki.sh)
- [`starter/ocsp.sh`](starter/ocsp.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/ocsp.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–4: the same revocation is recorded first
   - Lines 5–8: the client builds a request
   - Lines 9–13: signs an answer
   - Lines 14–17: checks the responder's signature
3. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash ocsp.sh
   ```

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m03l04-06` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
