# m05l04-06 · Counting the regulatory clock correctly

**Lesson:** [Incident Roles, Escalation & Crisis Comm](https://learnsome.tech/learn/cybersecurity-course/m05l04) (lesson 5.4, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can staff an incident with clear roles, apply a written escalation policy, and run crisis communication that meets regulatory deadlines.

In the lesson: Those clocks are strict. Under G D P R, a personal data breach must be reported to the supervisory authority without undue delay and, where feasible, within seventy two hours of becoming aware of it. The E U N I S two directive requires essential and important entities to send an early warning within twenty four hours of a significant incident, and a fuller notification within seventy two. The program takes the moment a German company became aware, a Friday afternoon in October. For each clock it adds the hours in U T C and converts back to Berlin time, and for contrast it also adds them to the local wall clock. Notice that every clock runs through the weekend. Notice too that the seventy two hour deadlines land at fifteen thirty, not sixteen thirty, because the clocks go back on the Sunday. Count in U T C, then convert.

## Files

- [`starter/deadlines.py`](starter/deadlines.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-06/starter`
2. Read `deadlines.py` the way the lesson builds it:
   - Lines 1–7: the moment a german company became aware
   - Lines 8–13: for each clock it adds the hours
3. Notes from the lesson:
   - Line 12: local wall-clock arithmetic ignores the DST change
4. Run it: `python3 deadlines.py`.
5. Check it from the repository root: `./check m05l04-06`.

## Expected output

```text
became aware        Fri 23 Oct 16:30 CEST
NIS2 early warning  Sat 24 Oct 16:30 CEST  wall-clock sum: 16:30
NIS2 notification   Mon 26 Oct 15:30 CET  wall-clock sum: 16:30
GDPR Art. 33 notice Mon 26 Oct 15:30 CET  wall-clock sum: 16:30
```

## How to check

`./check m05l04-06` copies `starter/` into a scratch directory and runs `python3 deadlines.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
