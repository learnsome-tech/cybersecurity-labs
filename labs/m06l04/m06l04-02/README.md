# m06l04-02 · Reading the certificate the service presents

**Lesson:** [Security Capstone Review & Certification](https://learnsome.tech/learn/cybersecurity-course/m06l04) (lesson 6.4, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can gather certificate and backup evidence, test it against written targets, turn the gaps into owned register entries, and choose a sensible next certification.

In the lesson: The booking team sends the certificate file. This short shell script asks openssl for the fields a reviewer reads. The first command prints the subject, the issuer, the validity dates and the subject alternative name, which is the name browsers actually match. Then the second pulls the key size and the signature algorithm out of the full text dump. And the last line hashes the file, so this exact certificate can go into the evidence pack. Run it. The name is right, and the signature uses S H A two five six. But the key is R S A with only one thousand and twenty four bits, below the two thousand and forty eight bit minimum in current standards, and the certificate expires on the nineteenth of October, less than three weeks after the review.

## Files

- [`starter/cert.pem`](starter/cert.pem)
- [`starter/command.txt`](starter/command.txt)
- [`starter/inspect_cert.sh`](starter/inspect_cert.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l04/m06l04-02/starter`
2. Read `inspect_cert.sh` the way the lesson builds it:
   - Lines 1–4: the first command prints the subject
   - Lines 5–6: the second pulls the key size
   - Lines 7: the last line hashes the file
3. Run it: `bash inspect_cert.sh`.
4. Check it from the repository root: `./check m06l04-02`.

## Expected output

```text
subject=O = Example Bookings Ltd, CN = booking.example.org
issuer=O = Example Bookings Ltd, CN = Example Bookings Internal CA
notBefore=Oct 20 00:00:00 2025 GMT
notAfter=Oct 19 23:59:59 2026 GMT
X509v3 Subject Alternative Name: 
DNS:booking.example.org
Public-Key: (1024 bit)
Signature Algorithm: sha256WithRSAEncryption
2d2c81214264862abcd5fc195870c69de5031951b5668f76b2e9b381316c8d26  cert.pem
```

## How to check

`./check m06l04-02` copies `starter/` into a scratch directory and runs `bash inspect_cert.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
