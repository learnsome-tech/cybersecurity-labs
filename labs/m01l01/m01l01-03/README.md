# m01l01-03 · A signature gives you non-repudiation

**Lesson:** [CIA Triad, Non-Repudiation & Parkerian Hexad](https://learnsome.tech/learn/cybersecurity-course/m01l01) (lesson 1.1, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can name which security property an incident broke, show why a shared key cannot give non-repudiation while a signature can, and trace identification, authentication, authorisation and accountability through a real auth.log.

In the lesson: Non-repudiation means the sender cannot credibly deny sending something, because only they could have produced the proof. That takes two different keys. This script uses openssl and generates an Ed twenty five five one nine key pair for Alice. She keeps the private key, and the bank only ever receives the public one. She signs the order. The bank verifies with the public key. Then the bank edits the account number and verifies again. The output reads success, then failure. The bank also cannot make a fresh signature for its edited order, because signing needs the private key it never had. The proof is only as good as Alice's control of that key. If it sits unprotected on a shared laptop, she can fairly argue that someone else signed.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/sign.sh`](starter/sign.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-03/starter`
2. Read `sign.sh` the way the lesson builds it:
   - Lines 1–2: generates an Ed twenty five five one nine key pair
   - Lines 3–6: She signs the order
   - Lines 7–10: verifies with the public key
   - Lines 11–15: edits the account number
3. Run it: `bash sign.sh`.
4. Check it from the repository root: `./check m01l01-03`.

## Expected output

```text
bank checks the order Alice signed:
Signature Verified Successfully
bank edits the account number and checks again:
Signature Verification Failure
```

## How to check

`./check m01l01-03` copies `starter/` into a scratch directory and runs `bash sign.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
