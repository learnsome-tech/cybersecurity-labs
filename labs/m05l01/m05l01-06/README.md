# m05l01-06 · Counting the nines

**Lesson:** [Business Impact Analysis, RTO & RPO Modeling](https://learnsome.tech/learn/cybersecurity-course/m05l01) (lesson 5.1, module 5: Resilience & Disaster Recovery) · Pro  
**Check:** Graded

## Goal

You can turn a business impact analysis into RTO and RPO targets, test them against real restore times and backup schedules, and work out what redundancy does to availability.

In the lesson: Let's put numbers on it. The avail function turns M T B F and M T T R in hours into the share of time a part is working. Series multiplies, because every part must be up. The pair function is the chance that both copies are not down at once, which is one minus the failure chance squared. The web tier, the database and the power feed get example figures, not industry data. One of everything gives just over ninety nine point two per cent, about seventy hours down a year. Doubling only the web servers helps, but the single database and power feed still dominate. Doubling everything brings it to about sixteen minutes. The catch sits in that squared term: it assumes the two copies fail independently. Two servers on one power strip do not.

## Files

- [`starter/availability.py`](starter/availability.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m05l01/m05l01-06/starter`
2. Read `availability.py` the way the lesson builds it:
   - Lines 1–4: the avail function
   - Lines 5–10: series multiplies
   - Lines 11–13: the pair function
   - Lines 14–21: example figures
3. Notes from the lesson:
   - Line 13: assumes the two copies fail independently
4. Run it: `python3 availability.py`.
5. Check it from the repository root: `./check m05l01-06`.

## Expected output

```text
one of everything  99.2047%  down about 4,180 min a year
two web servers    99.6982%  down about 1,586 min a year
two of everything  99.9970%  down about 16 min a year
```

## How to check

`./check m05l01-06` copies `starter/` into a scratch directory and runs `python3 availability.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m05l01) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
