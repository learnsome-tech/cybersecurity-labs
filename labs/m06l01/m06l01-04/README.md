# m06l01-04 · Private is not the same as allowed

**Lesson:** [Security Architecture Gap Analysis](https://learnsome.tech/learn/cybersecurity-course/m06l01) (lesson 6.1, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can compare exported security configuration against a written target architecture, find the gaps with a script, and rank them for a plan.

In the lesson: A common shortcut in gap reviews is to mark a rule as fine because the source is internal. This short program shows why that test is too weak. It takes the target, which is the app subnet, and a handful of sources. For each one it prints two answers: is the range private, and is it inside the target? All four internal ranges pass the first test, but only two pass the second. The ten slash eight block is private, yet it holds over sixteen million addresses, so every laptop, test server and forgotten build agent on the corporate network could reach the database. Private tells you how an address is routed. It says nothing about whether the architecture meant that host to connect.

## Files

- [`starter/private_vs_target.py`](starter/private_vs_target.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-04/starter`
2. Read `private_vs_target.py` the way the lesson builds it:
   - Lines 1–5: a handful of sources
   - Lines 6–11: it prints two answers
3. Run it: `python3 private_vs_target.py`.
4. Check it from the repository root: `./check m06l01-04`.

## Expected output

```text
10.20.1.0/24    private=True  inside target=True  addresses=256
10.20.1.128/25  private=True  inside target=True  addresses=128
10.20.2.0/24    private=True  inside target=False addresses=256
10.0.0.0/8      private=True  inside target=False addresses=16777216
0.0.0.0/0       private=False inside target=False addresses=4294967296
```

## How to check

`./check m06l01-04` copies `starter/` into a scratch directory and runs `python3 private_vs_target.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
