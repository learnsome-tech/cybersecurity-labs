# m03l04-03 · Four checks a client makes

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Runs, not graded

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: Now the client's side. This script rebuilds the same C A and certificate, then asks openssl verify the questions a browser asks, at fixed dates so the results never drift. The check function trusts only our root, through the C A file option, and prints the one line that matters. There is also an impostor: a certificate for the same name, signed by its own key. Run it. With the right name on the first of October, the certificate passes. Ask for shop dot example dot com and it fails with a hostname mismatch, because that name is not among the subject alternative names. On the first of January it has expired. The impostor fails as a self-signed certificate: the name is right and its signature is valid, but no trusted C A vouched for it. That is exactly the warning page a user should never click through.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/mkpki.sh`](starter/mkpki.sh)
- [`starter/verify.sh`](starter/verify.sh): the listing from the lesson
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-03/starter`
2. Read `verify.sh` the way the lesson builds it:
   - Lines 1–3: at fixed dates
   - Lines 4–9: the check function
   - Lines 10–13: there is also an impostor
   - Lines 14–18: run it
3. Run it: `bash verify.sh`.
4. Check it from the repository root: `./check m03l04-03`.

## What the lesson recorded

Shown for reference; the check does not compare it.

```text
right name:   www.pem: OK
wrong name:   hostname mismatch
after expiry: certificate has expired
self-signed:  self-signed certificate
```

## How to check

`./check m03l04-03` copies `starter/` into a scratch directory and runs `bash verify.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It runs without a pass or fail: what the listing prints in the lab sandbox differs from the output recorded for the lesson (it depends on the machine, the clock or the network), so the site runs it without a pass or fail. `./check` shows the output and the exit code.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
