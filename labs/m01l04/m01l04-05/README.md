# m01l04-05 · What the bastion's auth.log records

**Lesson:** [Defense-in-Depth & Security Control Categories](https://learnsome.tech/learn/cybersecurity-course/m01l04) (lesson 1.4, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can sort any control by category and type under both the ISC2 and Security+ schemes, and test one layer of a real defence in depth design, a fail2ban jail, against an auth.log to find the attacks it misses.

In the lesson: First, the evidence. The regular expression matches every Failed line in the bastion's auth dot log, whatever the method, and captures the timestamp and the source address. Syslog lines carry no year, so the program supplies one before parsing the time. Failures are grouped by address. Run as a script, it prints one line per address: how many failures and over what stretch of time. There are four sources. One outside address guessed seven user names in under a minute. A second tried six times over about an hour. An office address failed nine times as root in under three minutes. The last is alice, mistyping twice before getting in.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/failures.py`](starter/failures.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-05/starter`
2. Read `failures.py` the way the lesson builds it:
   - Lines 1–5: matches every Failed line
   - Lines 6–12: carry no year
   - Lines 13–17: one line per address
3. Run it: `python3 failures.py`.
4. Check it from the repository root: `./check m01l04-05`.

## Expected output

```text
203.0.113.66   7 failures between 02:14:00 and 02:14:42
198.51.100.23  6 failures between 02:15:00 and 03:20:00
192.0.2.15     9 failures between 02:19:00 and 02:21:40
203.0.113.9    2 failures between 08:31:02 and 08:31:09
```

## How to check

`./check m01l04-05` copies `starter/` into a scratch directory and runs `python3 failures.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
