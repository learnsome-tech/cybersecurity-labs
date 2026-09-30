# m05l02-02 · Would each site meet a six hour RTO?

**Lesson:** [Disaster Recovery Sites: Hot, Warm & Cold](https://learnsome.tech/learn/cybersecurity-course/m05l02) (lesson 5.2, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can choose between hot, warm and cold recovery sites by working out their real recovery time and data loss against a system's RTO and RPO, and plan how to test the choice.

In the lesson: Picking a site type starts with arithmetic. Take checkout from the business impact analysis, with a six hour R T O, and two terabytes of backups that must reach the recovery site over a one gigabit link. Two terabytes is sixteen thousand gigabits, and at one gigabit a second that is about four and a half hours of copying before anything else can happen. Each plan lists its steps with example durations; the three days for cold site hardware is an assumption to replace with your supplier's real answer. The loop totals each plan and names its slowest step. The cold site misses by days. The warm site misses too, and the reason is the copy, not the servers. That is the usual surprise: bandwidth into the recovery site often decides whether warm is good enough. Only the hot site meets the target, because its data is already there.

## Files

- [`starter/site_fit.py`](starter/site_fit.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l02/m05l02-02/starter`
2. Read `site_fit.py` the way the lesson builds it:
   - Lines 1–3: take checkout
   - Lines 4–5: two terabytes is sixteen thousand gigabits
   - Lines 6–13: each plan lists its steps
   - Lines 14–18: the loop totals each plan
3. Notes from the lesson:
   - Line 5: 2 TB = 16,000 Gbit; at 1 Gbit/s that is about 4.4 hours
4. Run it: `python3 site_fit.py`.
5. Check it from the repository root: `./check m05l02-02`.

## Expected output

```text
cold  90.4h  misses RTO 6h, slowest: deliver and rack hardware
warm   8.4h  misses RTO 6h, slowest: copy backups in
hot    0.5h  meets RTO 6h, slowest: switch DNS and test
```

## How to check

`./check m05l02-02` copies `starter/` into a scratch directory and runs `python3 site_fit.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l02) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
