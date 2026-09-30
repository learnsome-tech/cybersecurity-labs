# m03l02-04 · Signatures with RSA and Ed25519

**Lesson:** [Asymmetric Cryptography: RSA, ECC & Diffie-Hellman](https://learnsome.tech/learn/cybersecurity-course/m03l02) (lesson 3.2, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show two parties agreeing a key in public with Diffie-Hellman and X25519, compare RSA and elliptic curve key and signature sizes, and explain why authentication and forward secrecy still matter.

In the lesson: Signatures use the key pair the other way round. A release note gets signed twice, once with a three thousand and seventy two bit R S A key and once with Ed twenty five five one nine, an elliptic curve scheme. The check function asks openssl to verify using only the public key, which is all a customer would have. Inside the loop each key signs the file and we print the sizes. Look at the output. R S A needs a four hundred and twenty two byte public key and a three hundred and eighty four byte signature. Ed twenty five five one nine manages with forty four and sixty four, at a similar security level. Both verify. Then sed changes one character of the version number, and both signatures fail. That is integrity plus proof of origin, and because only the signer holds the private key, it supports non-repudiation as well.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/sign.sh`](starter/sign.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-04/starter`
2. Read `sign.sh` the way the lesson builds it:
   - Lines 1–4: signed twice
   - Lines 5–9: the check function
   - Lines 10–19: each key signs the file
   - Lines 20–22: sed changes one character
3. Run it: `bash sign.sh`.
4. Check it from the repository root: `./check m03l02-04`.

## Expected output

```text
rsa: public key 422 bytes, signature 384 bytes
  Signature Verified Successfully
ed: public key 44 bytes, signature 64 bytes
  Signature Verified Successfully
after the edit, rsa: Signature Verification Failure
after the edit, ed:  Signature Verification Failure
```

## How to check

`./check m03l02-04` copies `starter/` into a scratch directory and runs `bash sign.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
