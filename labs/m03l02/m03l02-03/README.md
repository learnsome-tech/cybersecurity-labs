# m03l02-03 · The same idea on an elliptic curve: X25519

**Lesson:** [Asymmetric Cryptography: RSA, ECC & Diffie-Hellman](https://learnsome.tech/learn/cybersecurity-course/m03l02) (lesson 3.2, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show two parties agreeing a key in public with Diffie-Hellman and X25519, compare RSA and elliptic curve key and signature sizes, and explain why authentication and forward secrecy still matter.

In the lesson: Now the elliptic curve version, using the openssl command. X twenty five five one nine is a curve widely used for key exchange in T L S. The loop gives Alice and Bob a key pair each and writes out the public halves. Then each side derives a secret from its own private key and the other side's public key, the same pattern as the Python program. Look at the sizes in the output. Bob's public key is forty four bytes, and that includes the encoding that names the algorithm. The Diffie-Hellman value was two hundred and fifty six bytes. The shared secret is thirty two bytes, and the compare step confirms both files are identical. Smaller keys for equal or better strength is the whole attraction of E C C: less data on the wire, and less work for a phone.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/ecdh.sh`](starter/ecdh.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l02/m03l02-03/starter`
2. Read `ecdh.sh` the way the lesson builds it:
   - Lines 1–5: a key pair each
   - Lines 6–9: each side derives a secret
   - Lines 10–14: look at the sizes
3. Run it: `bash ecdh.sh`.
4. Check it from the repository root: `./check m03l02-03`.

## Expected output

```text
Bob's public key on the wire: 44 bytes
shared secret: 32 bytes
Alice and Bob derived the same secret
```

## How to check

`./check m03l02-03` copies `starter/` into a scratch directory and runs `bash ecdh.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
