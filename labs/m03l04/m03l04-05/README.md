# m03l04-05 · Revoking a certificate with a CRL

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: Now the server's private key leaks. The certificate is still valid for weeks, so the C A has to revoke it. The configuration file beside this script names the C A database, and the revoke command marks serial one thousand as revoked for key compromise. Then the C A publishes a certificate revocation list, a C R L: a signed list of revoked serial numbers, valid here for one week. Next comes the same verify command, with and without the list. Look at the output. The list shows its update dates, serial one thousand, and the reason. Without the list, the stolen certificate still passes, which is the real weakness: a client that never checks revocation is fooled. With the C R L, verify reports certificate revoked. Lists grow over time and clients download them on a schedule, so there is always a window between revocation and the client noticing.

## Files

- [`starter/ca.cnf`](starter/ca.cnf)
- [`starter/command.txt`](starter/command.txt)
- [`starter/crl.sh`](starter/crl.sh): the listing from the lesson
- [`starter/mkpki.sh`](starter/mkpki.sh)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-05/starter`
2. Read `crl.sh` the way the lesson builds it:
   - Lines 1–6: the revoke command
   - Lines 7–11: publishes a certificate revocation list
   - Lines 12–16: with and without the list
3. Run it: `bash crl.sh`.
4. Check it from the repository root: `./check m03l04-05`.

## Expected output

```text
        Last Update: Oct 10 00:00:00 2026 GMT
        Next Update: Oct 17 00:00:00 2026 GMT
    Serial Number: 1000
                Key Compromise
without the CRL: www.pem: OK
error 23 at 0 depth lookup: certificate revoked
```

## How to check

It runs with OpenSSL 3.5 first on `PATH`, as on the site (the dev container has it).

`./check m03l04-05` copies `starter/` into a scratch directory and runs `bash crl.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
