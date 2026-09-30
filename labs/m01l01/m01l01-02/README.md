# m01l01-02 · A hash spots change; only a key spots a forger

**Lesson:** [CIA Triad, Non-Repudiation & Parkerian Hexad](https://learnsome.tech/learn/cybersecurity-course/m01l01) (lesson 1.1, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can name which security property an incident broke, show why a shared key cannot give non-repudiation while a signature can, and trace identification, authentication, authorisation and accountability through a real auth.log.

In the lesson: Integrity has a trap in it. Here is the payment order and a forged copy with a different account number. The first check sends a plain S H A two five six hash alongside the message. Anyone who can change the message can recompute the hash as well, so the forged order passes. Next, a keyed hash, called an H M A C. The sender and the bank share one secret key, and the verify function recomputes the tag with it. An attacker who has to guess the key produces a tag that fails. Now the catch. The bank holds the same key, so the bank can mint a valid tag for any message it likes. Run it and read the three lines: true, false, true. That last true is the gap we close next.

## Files

- [`starter/tags.py`](starter/tags.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l01/m01l01-02/starter`
2. Read `tags.py` the way the lesson builds it:
   - Lines 1–5: payment order and a forged copy
   - Lines 6–10: The first check
   - Lines 11–16: a keyed hash
   - Lines 17–21: Now the catch
3. Notes from the lesson:
   - Line 12: One shared key: either holder can make any tag
4. Run it: `python3 tags.py`.
5. Check it from the repository root: `./check m01l01-02`.

## Expected output

```text
sha256 matches forged order: True
hmac accepts attacker's tag: False
hmac accepts bank's own tag: True
```

## How to check

`./check m01l01-02` copies `starter/` into a scratch directory and runs `python3 tags.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
