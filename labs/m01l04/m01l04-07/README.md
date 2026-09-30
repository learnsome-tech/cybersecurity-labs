# m01l04-07 · Closing the gaps, and what it costs

**Lesson:** [Defense-in-Depth & Security Control Categories](https://learnsome.tech/learn/cybersecurity-course/m01l04) (lesson 1.4, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can sort any control by category and type under both the ISC2 and Security+ schemes, and test one layer of a real defence in depth design, a fail2ban jail, against an auth.log to find the attacks it misses.

In the lesson: Here is the fix as a reviewer would see it. diff shows two changed lines: findtime goes from ten minutes to sixty, and the office range comes out of ignoreip. Then the same checker runs against the new file. Now all three attackers are banned, the slow one at its fifth failure within the hour, and the office laptop at its fifth attempt, eighty seconds in. Alice is still fine. The cost is real, though. A wider window means staff who mistype a few times across an hour can get locked out, and those calls will reach the help desk. Taking the office out of ignoreip means an administrator can ban their own office. Somebody has to own that trade off and write it down.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/command.txt`](starter/command.txt)
- [`starter/failures.py`](starter/failures.py)
- [`starter/jail-fixed.local`](starter/jail-fixed.local)
- [`starter/jail.local`](starter/jail.local)
- [`starter/jail_check.py`](starter/jail_check.py)
- [`starter/retest.sh`](starter/retest.sh): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-07/starter`
2. Read `retest.sh` the way the lesson builds it:
   - Lines 1: diff shows
   - Lines 2: same checker
3. Run it: `bash retest.sh`.
4. Check it from the repository root: `./check m01l04-07`.

## Expected output

```text
4c4
< findtime = 10m
---
> findtime = 60m
7c7
< ignoreip = 127.0.0.1/8 192.0.2.0/24
---
> ignoreip = 127.0.0.1/8
203.0.113.66   banned at 02:14:28
198.51.100.23  banned at 03:07:00
192.0.2.15     banned at 02:20:20
203.0.113.9    not banned
```

## How to check

`./check m01l04-07` copies `starter/` into a scratch directory and runs `bash retest.sh` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
