# m04l02-04 · In use: tokenise what you store, mask what you show

**Lesson:** [Data States: Security at Rest, in Transit, and in Use](https://learnsome.tech/learn/cybersecurity-course/m04l02) (lesson 4.2, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can say which state a piece of data is in, which attacker that state invites, and which protection method fits it.

In the lesson: Data in use is the hardest state, because the application has to see real values to do its job. Two techniques shrink how many places hold them. The vault is a table mapping random tokens to card numbers; in production it is a separate, locked down service. Tokenise looks up the card, and if it is new, invents a random token with no mathematical link to the number. Mask keeps the last four digits and hides the rest, which is enough for an agent confirming which card a customer used. Three orders come in. The orders table stores only tokens, and because the same card always gets the same token, order one thousand and one and order one thousand and three can still be matched as one customer. Only the payments service may ask the vault for the real number. Steal the orders table and you get nothing to spend.

## Files

- [`starter/tokens.py`](starter/tokens.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l02/m04l02-04/starter`
2. Read `tokens.py` the way the lesson builds it:
   - Lines 1–4: The vault is a table
   - Lines 5–12: Tokenise looks up
   - Lines 13–14: Mask keeps
   - Lines 15–22: Three orders come in
3. Run it: `python3 tokens.py`.
4. Check it from the repository root: `./check m04l02-04`.

## Expected output

```text
1001 stored as tok_188d1398c8bcc939 support sees ************1111
1002 stored as tok_1d7daa34fecf8158 support sees ************4444
1003 stored as tok_188d1398c8bcc939 support sees ************1111
vault lookup by payments service: 5555555555554444
```

## How to check

`./check m04l02-04` copies `starter/` into a scratch directory and runs `python3 tokens.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
