# m03l03-05 · Hash chains: why a ledger shows tampering

**Lesson:** [Cryptographic Hashing: SHA-256, SHA-3 & Passwords](https://learnsome.tech/learn/cybersecurity-course/m03l03) (lesson 3.3, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show what SHA-256 and SHA-3 guarantee, use HMAC where a bare hash is forgeable, store passwords with salt and a slow function, and explain how a hash chain makes a ledger tamper-evident.

In the lesson: Chain hashes together and you get tamper evidence, the idea underneath a blockchain's open public ledger. Here are three payments. Each link hashes the previous link together with the new entry, starting from a string of zeros, so every link depends on everything before it. The published list stands for the copy every participant already holds. Then someone quietly changes the first payment from five to fifty and recomputes. Run it and look at the status column. Every link from the edit onwards is broken, not only the first. To hide the change, the forger would have to rewrite every later link and persuade every other copy holder to accept the new version. A blockchain adds rules for who may append and how the copies agree, but the tamper evidence itself comes from this chaining. Git history works the same way.

## Files

- [`starter/ledger.py`](starter/ledger.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-05/starter`
2. Read `ledger.py` the way the lesson builds it:
   - Lines 1–5: here are three payments
   - Lines 6–16: each link hashes the previous link
   - Lines 17–18: the published list
   - Lines 19–22: quietly changes the first payment
3. Run it: `python3 ledger.py`.
4. Check it from the repository root: `./check m03l03-05`.

## Expected output

```text
entry 0: published cf7cd4bf7343, recomputed 1dcae8da6c2e broken
entry 1: published a467cad5f3d3, recomputed f67a253ce887 broken
entry 2: published d6cf42652036, recomputed 337da3633b22 broken
```

## How to check

`./check m03l03-05` copies `starter/` into a scratch directory and runs `python3 ledger.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
