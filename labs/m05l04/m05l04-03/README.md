# m05l04-03 · Walking the chain at two in the morning

**Lesson:** [Incident Roles, Escalation & Crisis Comm](https://learnsome.tech/learn/cybersecurity-course/m05l04) (lesson 5.4, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can staff an incident with clear roles, apply a written escalation policy, and run crisis communication that meets regulatory deadlines.

In the lesson: This program loads the policy with tomllib, which has read TOML in the standard library since Python three point eleven. The page function takes a severity, the time the alert was raised, and who acknowledged when. It pages the first person in the chain and waits the escalation interval. If nobody has acknowledged, it pages the next one. The last lines run two alerts from the same night. The severity one alert pages the primary on-call at two fourteen, gets no answer, pages the incident commander at two nineteen, and the commander acknowledges at two twenty two. The severity three alert pages two people over thirty minutes, and then the chain runs out. Nobody else will ever be told. That is a gap in the policy, and the exercise asks you to close it.

## Files

- [`starter/escalate.py`](starter/escalate.py): the listing from the lesson
- [`starter/severity.toml`](starter/severity.toml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l04/m05l04-03/starter`
2. Read `escalate.py` the way the lesson builds it:
   - Lines 1–3: loads the policy with tomllib
   - Lines 4–7: the page function
   - Lines 8–10: it pages the first person
   - Lines 11–16: if nobody has acknowledged
   - Lines 17–19: the last lines run two alerts
3. Run it: `python3 escalate.py`.
4. Check it from the repository root: `./check m05l04-03`.

## Expected output

```text
02:14 sev1: customer data exposed or a core service down
  02:14 page primary on-call
  02:19 page incident commander
  02:22 acknowledged by incident commander
  comms: exec and status page update every 30 min
02:14 sev3: suspicious activity, nothing confirmed yet
  02:14 page primary on-call
  02:44 page secondary on-call
  nobody acknowledged and the chain has run out
```

## How to check

`./check m05l04-03` copies `starter/` into a scratch directory and runs `python3 escalate.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
