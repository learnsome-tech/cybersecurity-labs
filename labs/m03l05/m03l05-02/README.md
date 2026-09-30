# m03l05-02 · ML-KEM: key exchange built to survive Shor

**Lesson:** [Post-Quantum Cryptography & Key Lifecycles](https://learnsome.tech/learn/cybersecurity-course/m03l05) (lesson 3.5, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can explain what a quantum computer would break, run ML-KEM and ML-DSA and weigh their sizes, plan a hybrid migration, and rotate keys with envelope encryption.

In the lesson: M L KEM is a key encapsulation mechanism, and openssl includes it from version three point five. The shape differs slightly from Diffie-Hellman. Bob generates a key pair and publishes the public half. Alice runs encapsulate against it, which produces a fresh random secret for her and a ciphertext that only Bob's private key can open. Bob runs decapsulate and recovers the same secret. The last lines print the sizes and compare the two secrets. Look at the sizes. The public key is about twelve hundred bytes and the ciphertext just over a thousand, against forty four bytes for an X twenty five five one nine key. The shared secret is still thirty two bytes, ready to key A E S. Its security rests on a lattice problem called module learning with errors, for which no efficient quantum attack is known. The price is bandwidth, not speed: the operations are fast.

## Files

- [`starter/command.txt`](starter/command.txt)
- [`starter/mlkem.sh`](starter/mlkem.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-02/starter`
2. Read `mlkem.sh` the way the lesson builds it:
   - Lines 1–4: Bob generates a key pair
   - Lines 5–7: Alice runs encapsulate
   - Lines 8–9: Bob runs decapsulate
   - Lines 10–16: the last lines print the sizes
3. Run it: `bash mlkem.sh`.
4. Check it from the repository root: `./check m03l05-02`.

## Expected output

```text
public key, DER:     1206 bytes
ciphertext to Bob:   1088 bytes
shared secret:       32 bytes
Alice and Bob hold the same secret
```

## How to check

It runs with OpenSSL 3.5 first on `PATH`, as on the site (the dev container has it).

`./check m03l05-02` copies `starter/` into a scratch directory and runs `bash mlkem.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
