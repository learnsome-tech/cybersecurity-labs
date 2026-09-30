# m01l05-05 · Checking the standard against real behaviour

**Lesson:** [Security Governance vs Security Management](https://learnsome.tech/learn/cybersecurity-course/m01l05) (lesson 1.5, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can separate governance decisions from management work, place a document correctly among policy, standard, procedure and guideline, name the governance roles and external obligations, and produce compliance evidence that reflects how a system really behaves.

In the lesson: The standard becomes four measurable rules. The effective function reads the configuration the way sshd does: an Include is expanded in place, in sorted order, and for each keyword sshd keeps the first value it reads. setdefault gives exactly that behaviour. Then the program compares each rule with the effective value and names the file it came from. The result is one failure. Password authentication is yes, from the cloud init drop in, because it was read before the main file's no. On a real server you would take the effective settings straight from the daemon, by running s s h d with the capital T flag as root. The governance lesson is the same either way: evidence has to describe how the system behaves, not what a file appears to say.

## Files

- [`starter/check_standard.py`](starter/check_standard.py): the listing from the lesson
- [`starter/sshd_config`](starter/sshd_config)
- [`starter/sshd_config.d/50-cloud-init.conf`](starter/sshd_config.d/50-cloud-init.conf)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l05/m01l05-05/starter`
2. Read `check_standard.py` the way the lesson builds it:
   - Lines 1–4: The standard becomes
   - Lines 5–15: first value it reads
   - Lines 16–21: compares each rule
3. Run it: `python3 check_standard.py`.
4. Check it from the repository root: `./check m01l05-05`.

## Expected output

```text
pass permitrootlogin no from sshd_config
fail passwordauthentication yes from sshd_config.d/50-cloud-init.conf
pass x11forwarding no from sshd_config
pass maxauthtries 3 from sshd_config
```

## How to check

`./check m01l05-05` copies `starter/` into a scratch directory and runs `python3 check_standard.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
