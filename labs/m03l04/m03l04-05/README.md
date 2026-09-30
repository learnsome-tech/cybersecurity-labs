# m03l04-05 · Revoking a certificate with a CRL

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Read along

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: Now the server's private key leaks. The certificate is still valid for weeks, so the C A has to revoke it. The configuration file beside this script names the C A database, and the revoke command marks serial one thousand as revoked for key compromise. Then the C A publishes a certificate revocation list, a C R L: a signed list of revoked serial numbers, valid here for one week. Next comes the same verify command, with and without the list. Look at the output. The list shows its update dates, serial one thousand, and the reason. Without the list, the stolen certificate still passes, which is the real weakness: a client that never checks revocation is fooled. With the C R L, verify reports certificate revoked. Lists grow over time and clients download them on a schedule, so there is always a window between revocation and the client noticing.

## Files

- [`starter/ca.cnf`](starter/ca.cnf)
- [`starter/command.txt`](starter/command.txt)
- [`starter/crl.sh`](starter/crl.sh): the listing from the lesson
- [`starter/mkpki.sh`](starter/mkpki.sh)
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Read `starter/crl.sh` alongside the lesson.
2. Follow it the way the lesson builds it:
   - Lines 1–6: the revoke command
   - Lines 7–11: publishes a certificate revocation list
   - Lines 12–16: with and without the list
3. On a machine that has what it needs, the lesson ran it with:

   ```sh
   bash crl.sh
   ```

## How to check

**Read along.** The listing does not run cleanly in the lab sandbox (it relies on something the sandbox cannot provide), so the site shows it read-only.

There is nothing to check: `./check m03l04-05` says so and moves on.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
