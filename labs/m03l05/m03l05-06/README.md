# m03l05-06 · Envelope encryption: rotate without re-encrypting

**Lesson:** [Post-Quantum Cryptography & Key Lifecycles](https://learnsome.tech/learn/cybersecurity-course/m03l05) (lesson 3.5, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can explain what a quantum computer would break, run ML-KEM and ML-DSA and weigh their sizes, plan a hybrid migration, and rotate keys with envelope encryption.

In the lesson: Rotating a key that encrypted a terabyte database would mean re-encrypting the terabyte. Envelope encryption avoids that, and it is how cloud key management services work. A data encryption key, the D E K, encrypts the rows. A key encryption key, the K E K, which never leaves the key service, encrypts the D E K. The helper is the same libcrypto file from the symmetric lesson. Here the keys come from fixed labels so the output repeats, and every seal gets its own nonce. The row is sealed with the D E K, and the wrapped D E K is stored beside it. Now rotation: unwrap with version one, wrap again with version two. Run it and compare the lines. The row on disk never changed; only the wrapped D E K did, a few dozen bytes. The row still reads through version two, so version one can be retired. Destroy every wrapped copy of the D E K, and the row is gone for good.

## Files

- [`starter/aead.py`](starter/aead.py)
- [`starter/envelope.py`](starter/envelope.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l05/m03l05-06/starter`
2. Read `envelope.py` the way the lesson builds it:
   - Lines 1–10: here the keys come from fixed labels
   - Lines 11–15: the wrapped D E K is stored beside it
   - Lines 16–22: now rotation
3. Run it: `python3 envelope.py`.
4. Check it from the repository root: `./check m03l05-06`.

## Expected output

```text
row on disk:       6fc83048bf2669656479163ee2adbed96b63ebde...
DEK wrapped by v1: 654c5fc8646b8eb17e46633d522ce22eedf7471e...
DEK wrapped by v2: 763b71c82367d6c2a9c0644ccd3dcf3a9d837d06...
row reads as:      order 1042: deliver to 221B Baker St
```

## How to check

It runs with OpenSSL 3.5 first on `PATH`, as on the site (the dev container has it).

`./check m03l05-06` copies `starter/` into a scratch directory and runs `python3 envelope.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
