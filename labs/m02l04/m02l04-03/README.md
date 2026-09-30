# m02l04-03 · Finding card numbers in a support export

**Lesson:** [Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS](https://learnsome.tech/learn/cybersecurity-course/m02l04) (lesson 2.4, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tell which of SOC 2, HIPAA, GDPR and PCI DSS applies and why, find card data that has leaked into scope, and work out the breach notification deadlines one incident triggers.

In the lesson: Support tools are a classic leak. This is an export of ticket notes. The program looks for runs of thirteen to nineteen digits, allowing a space or dash between them, which is how people really type card numbers. Every candidate goes through the Luhn check, the checksum built into every card number, which weeds out order and phone numbers. The loop never prints the full number: only the first six and last four digits, the usual masked form PCI DSS allows for people with no business need to see more. Run it. Two card numbers, public test numbers here, but in production that pulls the whole ticketing system into scope. Two order numbers fail the checksum and are left alone. The fix belongs upstream: mask the chat field before anything is saved.

## Files

- [`starter/pan_scan.py`](starter/pan_scan.py): the listing from the lesson
- [`starter/support_export.log`](starter/support_export.log)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-03/starter`
2. Read `pan_scan.py` the way the lesson builds it:
   - Lines 1–4: looks for runs of thirteen to nineteen digits
   - Lines 5–11: the Luhn check
   - Lines 12–18: never prints the full number
3. Run it: `python3 pan_scan.py`.
4. Check it from the repository root: `./check m02l04-03`.

## Expected output

```text
line 1: 773022******4408  fails Luhn, not a card
line 2: 411111******1111  card number
line 3: 502188******2256  fails Luhn, not a card
line 4: 555555******4444  card number
```

## How to check

`./check m02l04-03` copies `starter/` into a scratch directory and runs `python3 pan_scan.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
