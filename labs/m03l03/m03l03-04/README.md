# m03l03-04 · Passwords: fast hashes fall, salted slow ones hold

**Lesson:** [Cryptographic Hashing: SHA-256, SHA-3 & Passwords](https://learnsome.tech/learn/cybersecurity-course/m03l03) (lesson 3.3, module 3: Applied Cryptography & Keys) · Pro  
**Check:** Graded

## Goal

You can show what SHA-256 and SHA-3 guarantee, use HMAC where a bare hash is forgeable, store passwords with salt and a slow function, and explain how a hash chain makes a ledger tamper-evident.

In the lesson: Passwords are where plain hashing does real damage. Three users, and two of them chose the same password. The mistake stores one fast, unsalted SHA two fifty six each. If that table leaks, the attacker hashes a wordlist once and looks every user up in it, and a graphics card manages billions of those guesses a second. The fix has two parts. A unique random salt per user, stored beside the hash, so equal passwords give different records and no precomputed table covers everyone. The salts here are fixed only so the output repeats. Then key stretching: a deliberately slow function. Scrypt with these settings needs sixteen mebibytes of memory per guess, which is exactly what graphics cards are short of. Now run it. Amara and Ben share a hash and fall together; only Chen, with a long random password, survives. Under scrypt their records look unrelated. Argon two i d, bcrypt and P B K D F two do the same job.

## Files

- [`starter/passwords.py`](starter/passwords.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m03l03/m03l03-04/starter`
2. Read `passwords.py` the way the lesson builds it:
   - Lines 1–4: two of them chose the same password
   - Lines 5–11: the mistake stores one fast
   - Lines 12–21: the fix has two parts
3. Run it: `python3 passwords.py`.
4. Check it from the repository root: `./check m03l03-04`.

## Expected output

```text
amara and ben share a hash: True
  amara: Summer2026!
  ben: Summer2026!
  chen: not in the wordlist
  amara: scrypt 16bd93c3c924cc9f0cd639541e0e3696...
  ben: scrypt 0180ddc819d35049444a09ba4a3ecf50...
memory per guess: 16 MiB
```

## How to check

`./check m03l03-04` copies `starter/` into a scratch directory and runs `python3 passwords.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m03l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
