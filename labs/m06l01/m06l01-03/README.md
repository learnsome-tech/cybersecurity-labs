# m06l01-03 · Checking every rule against the target

**Lesson:** [Security Architecture Gap Analysis](https://learnsome.tech/learn/cybersecurity-course/m06l01) (lesson 6.1, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can compare exported security configuration against a written target architecture, find the gaps with a script, and rank them for a plan.

In the lesson: The target state goes at the top as data, one line per requirement. Requirement S E G zero one says Postgres may only be reached from the app subnet. S E G zero two says S S H may only come from the management subnet. Next, the covers function decides whether a permission reaches a port. Protocol minus one covers everything, which is the case people forget. Otherwise the port must sit inside the from and to range. Then the loop walks every group, every permission and every source range, and asks the standard library ipaddress module one precise question: is this source network a subnet of an allowed network? Run it. Two lines are met and four are gaps. One of them is a surprise: the migration rule on the database tier also opens S S H, because all traffic includes port twenty two.

## Files

- [`starter/gap_check.py`](starter/gap_check.py): the listing from the lesson
- [`starter/sg.json`](starter/sg.json)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l01/m06l01-03/starter`
2. Read `gap_check.py` the way the lesson builds it:
   - Lines 1–6: the target state goes at the top as data
   - Lines 7–11: the covers function decides
   - Lines 12–22: the loop walks every group
3. Notes from the lesson:
   - Line 9: -1 matches every protocol and port, so it passes any port test
   - Line 20: subnet_of: is the whole source range inside an allowed range?
4. Run it: `python3 gap_check.py`.
5. Check it from the repository root: `./check m06l01-03`.

## Expected output

```text
SEG-01 db-tier 5432 10.20.1.0/24 met
SEG-01 db-tier 5432 203.0.113.40/32 gap: vendor BI
SEG-01 db-tier 5432 10.0.0.0/8 gap: migration
SEG-02 db-tier 22 10.0.0.0/8 gap: migration
SEG-02 bastion 22 10.20.9.0/24 met
SEG-02 bastion 22 0.0.0.0/0 gap: temp debug
```

## How to check

`./check m06l01-03` copies `starter/` into a scratch directory and runs `python3 gap_check.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
