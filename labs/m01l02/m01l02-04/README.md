# m01l02-04 · Opportunistic noise or a chosen target

**Lesson:** [Threat Actors, Motivations & Cyber Kill Chain](https://learnsome.tech/learn/cybersecurity-course/m01l02) (lesson 1.2, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can tell threat actors apart by resources, skill and motive, spot a targeted visitor among scanner noise in a web log, and place incident evidence on the seven steps of the Cyber Kill Chain to see where it could have been stopped.

In the lesson: The regular expression pulls the address, time, method, path and status out of each line, and the loop groups the requests by address. For each address the program counts three things: requests for pages that do not exist, requests for pages about the company and its people, and login attempts. If every request missed, the client was working through the same list it tries on every server on the internet. If it read up on staff and then tried to log in, somebody chose us. Two addresses are opportunistic, one is targeted, one is ordinary. The log cannot tell you whether the targeted one is a criminal gang or a foreign service. It tells you someone studied the accounts team, and that is where the phishing email will land.

## Files

- [`starter/access.log`](starter/access.log)
- [`starter/triage.py`](starter/triage.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l02/m01l02-04/starter`
2. Read `triage.py` the way the lesson builds it:
   - Lines 1–5: The regular expression
   - Lines 6–10: groups the requests
   - Lines 11–15: counts three things
   - Lines 16–22: If every request missed
3. Run it: `python3 triage.py`.
4. Check it from the repository root: `./check m01l02-04`.

## Expected output

```text
192.0.2.7     requests: 2  opportunistic: asked only for software we do not run
192.0.2.99    requests: 2  opportunistic: asked only for software we do not run
192.0.2.66    requests: 4  targeted: read up on our staff, then tried to log in
192.0.2.51    requests: 1  nothing unusual
```

## How to check

`./check m01l02-04` copies `starter/` into a scratch directory and runs `python3 triage.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
