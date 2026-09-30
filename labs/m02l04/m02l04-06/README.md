# m02l04-06 · One incident, several notification clocks

**Lesson:** [Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS](https://learnsome.tech/learn/cybersecurity-course/m02l04) (lesson 2.4, module 2: Governance, Risk & Compliance) · Pro  
**Check:** Graded

## Goal

You can tell which of SOC 2, HIPAA, GDPR and PCI DSS applies and why, find card data that has leaked into scope, and work out the breach notification deadlines one incident triggers.

In the lesson: Both laws start a clock when a breach happens. Take one incident at a telehealth company with patients in Europe and the United States. The program records the moment the company became aware and how many people were affected where. GDPR says tell the supervisory authority without undue delay and, where feasible, within seventy two hours of becoming aware. HIPAA says tell individuals without unreasonable delay and no later than sixty calendar days after discovery. If five hundred or more are affected, the Secretary of Health and Human Services is told on the same timeline; smaller breaches go in a yearly log. More than five hundred residents of one state also means notifying prominent media there. Run it. Three days for Europe, mid July for patients, and a media notice in California. Individual states add breach laws of their own, so legal counsel owns the final list.

## Files

- [`starter/breach_clock.py`](starter/breach_clock.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m02l04/m02l04-06/starter`
2. Read `breach_clock.py` the way the lesson builds it:
   - Lines 1–5: records the moment the company became aware
   - Lines 6–7: seventy two hours
   - Lines 8–12: on the same timeline
   - Lines 13–16: prominent media
3. Run it: `python3 breach_clock.py`.
4. Check it from the repository root: `./check m02l04-06`.

## Expected output

```text
GDPR supervisory authority by 2026-05-17 16:20:00+00:00
HIPAA individuals no later than 2026-07-13
HIPAA HHS Secretary: same deadline, 760 individuals
HIPAA media notice in CA: 620 residents
```

## How to check

`./check m02l04-06` copies `starter/` into a scratch directory and runs `python3 breach_clock.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m02l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
