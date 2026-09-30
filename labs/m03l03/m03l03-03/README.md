# m03l03-03 · Integrity needs a key: HMAC

**Lesson:** [Cryptographic Hashing: SHA-256, SHA-3 & Passwords](https://learnsome.tech/learn/cybersecurity-course/m03l03) (lesson 3.3, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show what SHA-256 and SHA-3 guarantee, use HMAC where a bare hash is forgeable, store passwords with salt and a slow function, and explain how a hash chain makes a ledger tamper-evident.

In the lesson: A digest proves integrity only if the attacker cannot replace it. Here is a payment webhook. Sender and receiver share a secret, and the sender puts an H M A C of the body in a header, the same shape GitHub uses in its X Hub Signature two five six header. The first check is the mistake: it compares the header with a plain SHA two fifty six of the body. The second recomputes the H M A C with the secret and compares with compare digest, which takes the same time wherever the strings differ, so response timing leaks nothing. Now the attacker changes the amount to one penny and writes a fresh plain hash. Run it. The plain check accepts the forgery, because anyone can compute SHA two fifty six. The H M A C check rejects it, because the attacker does not have the key.

## Files

- [`starter/webhook.py`](starter/webhook.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-03/starter`
2. Read `webhook.py` the way the lesson builds it:
   - Lines 1–6: the sender puts an H M A C
   - Lines 7–11: the first check is the mistake
   - Lines 12–16: the second recomputes
   - Lines 17–22: changes the amount to one penny
3. Run it: `python3 webhook.py`.
4. Check it from the repository root: `./check m03l03-03`.

## Expected output

```text
genuine request, HMAC check:   True
forged request, plain check:   True
forged request, HMAC check:    False
```

## How to check

`./check m03l03-03` copies `starter/` into a scratch directory and runs `python3 webhook.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
