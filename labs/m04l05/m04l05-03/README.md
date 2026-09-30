# m04l05-03 · Pattern plus validation: finding card numbers

**Lesson:** [Data Loss Prevention & Egress Monitoring](https://learnsome.tech/learn/cybersecurity-course/m04l05) (lesson 4.5, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can explain how a DLP rule decides that outbound content is sensitive, tune it against false positives, and spot bulk exfiltration in connection logs.

In the lesson: Here is how a card number rule works inside most D L P engines, in a few lines of Python applying the same logic. The pattern finds thirteen to nineteen digits, allowing spaces or dashes between them. That alone would fire on order numbers, invoice numbers and tracking codes. So every candidate goes through a check digit test. The Luhn function doubles every second digit from the right, adds everything up, and a real card number always gives a multiple of ten. The program skips the headers and reads the email body. The output shows four sixteen digit matches, and only the two real test card numbers pass. The order and invoice numbers fail the check, and a rule that skipped it would have blocked a normal business email and taught staff to ignore alerts.

## Files

- [`starter/cards.py`](starter/cards.py): the listing from the lesson
- [`starter/outbound.eml`](starter/outbound.eml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-03/starter`
2. Read `cards.py` the way the lesson builds it:
   - Lines 1–2: The pattern
   - Lines 3–11: The Luhn function
   - Lines 12–17: reads the email body
3. Run it: `python3 cards.py`.
4. Check it from the repository root: `./check m04l05-03`.

## Expected output

```text
4000 1234 5678 9011    fails Luhn, not a card
7712-3400-9981-2265    fails Luhn, not a card
4111 1111 1111 1111    card number
5555-5555-5555-4444    card number
```

## How to check

`./check m04l05-03` copies `starter/` into a scratch directory and runs `python3 cards.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
