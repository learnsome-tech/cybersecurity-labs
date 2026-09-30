# m03l03-02 · SHA-256 and SHA-3 on a one-character change

**Lesson:** [Cryptographic Hashing: SHA-256, SHA-3 & Passwords](https://learnsome.tech/learn/cybersecurity-course/m03l03) (lesson 3.3, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show what SHA-256 and SHA-3 guarantee, use HMAC where a bare hash is forgeable, store passwords with salt and a slow function, and explain how a hash chain makes a ledger tamper-evident.

In the lesson: Two payment lines that differ in one character, a one against a nine, plus ten megabytes of zeros. For each algorithm we hash both lines, then count how many of the two hundred and fifty six output bits changed. SHA two fifty six is the familiar member of the SHA two family. SHA three is a completely different design, called Keccak, which NIST standardised as an alternative in case SHA two is ever weakened. Run it and read the bit counts. One changed character flips about half the output bits, one hundred and thirty one for one algorithm and one hundred and twenty three for the other. That is the avalanche effect: similar inputs give unrelated digests, so a digest tells an attacker nothing about how close a guess is. And ten megabytes in still gives thirty two bytes out.

## Files

- [`starter/fingerprint.py`](starter/fingerprint.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-02/starter`
2. Read `fingerprint.py` the way the lesson builds it:
   - Lines 1–5: two payment lines that differ
   - Lines 6–10: then count how many
   - Lines 11–15: SHA three is a completely different design
3. Run it: `python3 fingerprint.py`.
4. Check it from the repository root: `./check m03l03-02`.

## Expected output

```text
sha256 of a: 1ee0aeb4579f4ccc525673666f4a844f63c6925c...
sha256 of b: ecd3551614ac649d22868c9c8830ae9325a2d270...
  131 of 256 bits differ
  ten megabytes in, 32 bytes out
sha3_256 of a: 2a8192544d2fec85b1994cdbc6fb4e45d324fa47...
sha3_256 of b: 378205ce9bcf621b7705f1944bbf87c69bd3b697...
  123 of 256 bits differ
  ten megabytes in, 32 bytes out
```

## How to check

`./check m03l03-02` copies `starter/` into a scratch directory and runs `python3 fingerprint.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
