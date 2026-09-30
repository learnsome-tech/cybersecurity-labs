# m03l04-06 · OCSP: one question, one signed answer

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: The online certificate status protocol, O C S P, asks about one certificate instead of downloading a whole list. It normally runs over H T T P; here the request and response are files, so each step is visible without a network. The same revocation is recorded first. The client builds a request naming the issuer and the serial number. The responder looks the serial up in the C A database and signs an answer. Then the client checks the responder's signature and reads the status. Run it. Response verify O K, then revoked, reason key compromise. Plain O C S P has two problems: every lookup tells the responder which site you are visiting, and when the responder is down, browsers usually carry on anyway. O C S P stapling fixes the first: the server fetches this signed response itself and sends it inside the T L S handshake.

## Files

- [`starter/ca.cnf`](starter/ca.cnf)
- [`starter/command.txt`](starter/command.txt)
- [`starter/mkpki.sh`](starter/mkpki.sh)
- [`starter/ocsp.sh`](starter/ocsp.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-06/starter`
2. Read `ocsp.sh` the way the lesson builds it:
   - Lines 1–4: the same revocation is recorded first
   - Lines 5–8: the client builds a request
   - Lines 9–13: signs an answer
   - Lines 14–17: checks the responder's signature
3. Run it: `bash ocsp.sh`.
4. Check it from the repository root: `./check m03l04-06`.

## Expected output

```text
          Serial Number: 1000
    OCSP Response Status: successful (0x0)
    Cert Status: revoked
Response verify OK
www.pem: revoked
	Reason: keyCompromise
```

## How to check

It runs with OpenSSL 3.5 first on `PATH`, as on the site (the dev container has it).

`./check m03l04-06` copies `starter/` into a scratch directory and runs `bash ocsp.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
