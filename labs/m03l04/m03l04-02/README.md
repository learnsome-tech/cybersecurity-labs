# m03l04-02 · Build a CA, request a certificate, issue it

**Lesson:** [Public Key Infrastructure: X.509 Certificates & CAs](https://learnsome.tech/learn/cybersecurity-course/m03l04) (lesson 3.4, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can build a CA, turn a CSR into an X.509 certificate, predict how a client's chain, name and date checks will fail, and revoke a certificate with a CRL and OCSP.

In the lesson: Here is the whole process on one screen, using the openssl command. First the certificate authority. It makes a key pair and a root certificate that it signs itself, marked with basic constraints as a C A and valid for ten years. Then the server. It makes its own key pair, which never leaves it, and a certificate signing request, a C S R, carrying its name and the subject alternative names it wants: www dot example dot com and the bare domain. The request is signed with the server's private key, which proves the requester holds that key. Then the C A signs a certificate, copying the requested names across, with serial number four thousand and ninety six and ninety days of validity. The last command prints the fields worth reading. Read the output from the top. The C A first confirms the request's signature. Then come issuer, subject, the serial in hexadecimal, the dates, and the names a browser will match.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/mkpki.sh`](starter/mkpki.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l04/m03l04-02/starter`
2. Read `mkpki.sh` the way the lesson builds it:
   - Lines 1–7: first the certificate authority
   - Lines 8–11: then the server
   - Lines 12–15: then the C A signs a certificate
   - Lines 16–17: the last command prints
3. Run it: `bash mkpki.sh`.
4. Check it from the repository root: `./check m03l04-02`.

## Expected output

```text
issuer=O=Example Corp, CN=Example Corp Root CA
subject=CN=www.example.com
serial=1000
notBefore=Sep  1 00:00:00 2026 GMT
notAfter=Nov 30 00:00:00 2026 GMT
X509v3 Subject Alternative Name: 
    DNS:www.example.com, DNS:example.com
Certificate request self-signature ok
subject=CN=www.example.com
```

## How to check

It runs with OpenSSL 3.5 first on `PATH`, as on the site (the dev container has it).

`./check m03l04-02` copies `starter/` into a scratch directory and runs `bash mkpki.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
