# m01l02-06 · Placing an incident on the chain

**Lesson:** [Threat Actors, Motivations & Cyber Kill Chain](https://learnsome.tech/learn/cybersecurity-course/m01l02) (lesson 1.2, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can tell threat actors apart by resources, skill and motive, spot a targeted visitor among scanner noise in a web log, and place incident evidence on the seven steps of the Cyber Kill Chain to see where it could have been stopped.

In the lesson: The program lists the seven phases, then loads a timeline an analyst assembled after a ransomware incident: one row per piece of evidence, each tagged with a phase and with whether an alert fired at the time. For each phase it finds the matching rows. Weaponisation has none, and never will, because it happened on the attacker's machine. Otherwise it prints when the phase was first seen, and whether anything alerted. Read the result. Every phase from reconnaissance to command and control is in the logs, and every one was missed. The only alert came from endpoint detection when files were being renamed in bulk. The last line is dwell time, how long the attacker was inside before anyone knew. Almost six days, and each missed row was a chance to cut the chain.

## Files

- [`starter/killchain.py`](starter/killchain.py): the listing from the lesson
- [`starter/timeline.csv`](starter/timeline.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-06/starter`
2. Read `killchain.py` the way the lesson builds it:
   - Lines 1–5: lists the seven phases
   - Lines 6: loads a timeline
   - Lines 7–14: For each phase
   - Lines 15–19: The last line is dwell time
3. Run it: `python3 killchain.py`.
4. Check it from the repository root: `./check m01l02-06`.

## Expected output

```text
reconnaissance         2026-09-01T09:40 missed
weaponisation          nothing in our logs
delivery               2026-09-03T08:59 missed
exploitation           2026-09-03T09:07 missed
installation           2026-09-03T09:08 missed
command and control    2026-09-03T09:10 missed
actions on objectives  2026-09-08T22:15 alert
first alert at 2026-09-09T03:30 which is 5 days, 18:31:00 after delivery
```

## How to check

`./check m01l02-06` copies `starter/` into a scratch directory and runs `python3 killchain.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
