# m01l04-06 · Applying the jail's rule to the log

**Lesson:** [Defense-in-Depth & Security Control Categories](https://learnsome.tech/learn/cybersecurity-course/m01l04) (lesson 1.4, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can sort any control by category and type under both the ISC2 and Security+ schemes, and test one layer of a real defence in depth design, a fail2ban jail, against an auth.log to find the attacks it misses.

In the lesson: The checker imports those failures. configparser reads the jail file, and the S S H section inherits the defaults, just as fail to ban does. This sketch only understands minutes for findtime. The ignore list becomes network objects from the ipaddress module, with strict turned off, because one twenty seven dot nought dot nought dot one slash eight has host bits set and fail to ban accepts it anyway. Any address inside those networks is skipped entirely. For the rest, the program slides along the failures and bans when any five consecutive failures fit inside ten minutes. Only the fast outsider is banned. The slow guesser never gets five into one window. The office laptop, which is the most worrying line in the log, is never even considered. Alice is left alone, which is correct.

## Files

- [`starter/auth.log`](starter/auth.log)
- [`starter/command.txt`](starter/command.txt)
- [`starter/failures.py`](starter/failures.py)
- [`starter/jail.local`](starter/jail.local)
- [`starter/jail_check.py`](starter/jail_check.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l04/m01l04-06/starter`
2. Read `jail_check.py` the way the lesson builds it:
   - Lines 1–9: configparser reads
   - Lines 10–13: only understands minutes
   - Lines 14–18: skipped entirely
   - Lines 19–21: any five consecutive failures
3. Run it: `python3 jail_check.py jail.local`.
4. Check it from the repository root: `./check m01l04-06`.

## Expected output

```text
203.0.113.66   banned at 02:14:28
198.51.100.23  not banned
192.0.2.15     never banned: inside ignoreip
203.0.113.9    not banned
```

## How to check

`./check m01l04-06` copies `starter/` into a scratch directory and runs `python3 jail_check.py jail.local` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l04) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
