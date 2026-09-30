# m02l05-06 · Verifying an SLA from the vendor's own incident export

**Lesson:** [Vendor & Third-Party Risk Management Programs](https://learnsome.tech/learn/cybersecurity-course/m02l05) (lesson 2.5, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tier vendors by the risk they bring, choose the evidence and contract terms each tier needs, check a vendor's SBOM against advisories, and verify their SLA with your own data.

In the lesson: Here is that check. The vendor's status page exports every incident from August as a spreadsheet file. The top of the program holds the month's length and the service level schedule copied from our agreement: ninety nine point nine per cent, a credit below that line and a larger one below ninety nine. Then the loop measures each incident and counts only full outages, because our contract excludes announced maintenance and degraded performance. Finally it computes availability and the credit due. Run it. Fifty eight minutes of outage against an allowance of under forty five. Availability lands just under target, so a ten per cent credit is owed, and nobody would have claimed it without this check. Notice how much rests on definitions. If degraded time counted, the figure would be worse. Read what downtime means before you sign.

## Files

- [`starter/sla.py`](starter/sla.py): the listing from the lesson
- [`starter/status_export_2026-08.csv`](starter/status_export_2026-08.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l05/m02l05-06/starter`
2. Read `sla.py` the way the lesson builds it:
   - Lines 1–5: the service level schedule copied from our agreement
   - Lines 6–14: the loop measures each incident
   - Lines 15–20: computes availability
3. Run it: `python3 sla.py`.
4. Check it from the repository root: `./check m02l05-06`.

## Expected output

```text
04 Aug 02:00 maintenance  90 min
12 Aug 14:05 outage       36 min  counted
19 Aug 09:10 degraded     22 min
27 Aug 22:50 outage       22 min  counted
58 min counted as down, 44.6 allowed
availability 99.870%, credit due 10% of the fee
```

## How to check

`./check m02l05-06` copies `starter/` into a scratch directory and runs `python3 sla.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
