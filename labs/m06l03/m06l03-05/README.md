# m06l03-05 · Testing each sampled change against the policy

**Lesson:** [Internal Audits, Sampling & Evidence Chains](https://learnsome.tech/learn/cybersecurity-course/m06l03) (lesson 6.3, module 6: Enterprise Strategy & Audit) · Pro  
**Check:** Graded

## Goal

You can draw a repeatable audit sample from a complete population, test it against a control statement, seal the evidence with hashes, and write up the finding.

In the lesson: Each sampled ticket is tested against the three parts of the policy statement. Was an approval recorded? Is the approver someone other than the implementer? And was the approval given before the change was deployed? Comparing the timestamps as text works here because they all share one fixed format that sorts in time order. Every result is written to a results file, pass or exception, because the passes are evidence too. Two of fifteen fail. Ticket ten nineteen was approved and deployed by the same engineer, and ticket ten thirty one was approved the day after it went live. With zero exceptions tolerated, the control did not operate effectively. Ticket ten twenty six, which the sample never picked, shows the problem is wider still.

## Files

- [`starter/changes.csv`](starter/changes.csv)
- [`starter/sample.txt`](starter/sample.txt)
- [`starter/test_sample.py`](starter/test_sample.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m06l03/m06l03-05/starter`
2. Read `test_sample.py` the way the lesson builds it:
   - Lines 1–9: each sampled ticket is tested
   - Lines 10–17: was an approval recorded
   - Lines 18–22: every result is written to a results file
3. Notes from the lesson:
   - Line 14: Timestamps in one fixed ISO 8601 format compare correctly as text
4. Run it: `python3 test_sample.py`.
5. Check it from the repository root: `./check m06l03-05`.

## Expected output

```text
CHG-1019 approved by the person who deployed it 2026-05-27T09:45 2026-05-28T10:00
CHG-1031 approved after it was deployed 2026-07-14T05:45 2026-07-13T03:45
2 exception(s) in 15 tested; tolerable exceptions: 0
```

## How to check

`./check m06l03-05` copies `starter/` into a scratch directory and runs `python3 test_sample.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m06l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
