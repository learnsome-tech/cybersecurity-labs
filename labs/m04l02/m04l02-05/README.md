# m04l02-05 · Hashing is not hiding when inputs are guessable

**Lesson:** [Data States: Security at Rest, in Transit, and in Use](https://learnsome.tech/learn/cybersecurity-course/m04l02) (lesson 4.2, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can say which state a piece of data is in, which attacker that state invites, and which protection method fits it.

In the lesson: Teams often hash personal fields before sharing an export, and call it anonymised. Here is why that fails for small sets of values. The program has a secret key, which in real life stays in a key manager, and two ways to hash: plain S H A two fifty six, and an H M A C using that key. The guess function tries every date from nineteen twenty to twenty ten, about thirty three thousand of them, and compares hashes. The last two lines hash one date of birth each way and hand it to someone who only has the export. Plain hashing falls in well under a second: the output shows it recovered the date. The keyed version survives, because without the key the attacker cannot compute a single matching value. Postcodes, phone numbers and dates of birth all have this problem.

## Files

- [`starter/hashes.py`](starter/hashes.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-05/starter`
2. Read `hashes.py` the way the lesson builds it:
   - Lines 1–2: a secret key
   - Lines 3–8: two ways to hash
   - Lines 9–17: The guess function
   - Lines 18–20: hash one date of birth
3. Run it: `python3 hashes.py`.
4. Check it from the repository root: `./check m04l02-05`.

## Expected output

```text
plain SHA-256: recovered 1987-03-14 after 24545 guesses
HMAC, key unknown: no match after 33238 guesses
```

## How to check

`./check m04l02-05` copies `starter/` into a scratch directory and runs `python3 hashes.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
