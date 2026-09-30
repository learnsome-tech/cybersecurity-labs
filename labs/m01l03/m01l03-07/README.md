# m01l03-07 · Scoring a phishing simulation

**Lesson:** [Social Engineering, Phishing & Human Defense](https://learnsome.tech/learn/cybersecurity-course/m01l03) (lesson 1.3, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can name the common attack vectors and social engineering techniques, read a suspicious email's raw headers and authentication results, spot lookalike domains, and judge a phishing awareness programme by how fast people report.

In the lesson: Here are the results of a simulated invoice lure sent to ten people, one row per person with the time of each action. The program counts clicks, submitted passwords and reports. Then it finds the first report and measures it from the moment of sending. Last, it lists who clicked and then reported anyway. Four people clicked, two typed a password, four reported. The first report came four minutes in, while the last click came an hour and forty minutes later. Acted on quickly, that one report protects everyone who had not yet opened it. And dev, who clicked and then reported, is the behaviour you want most. Treat that person as a success, or next time they will stay quiet.

## Files

- [`starter/campaign.py`](starter/campaign.py): the listing from the lesson
- [`starter/results.csv`](starter/results.csv)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-07/starter`
2. Read `campaign.py` the way the lesson builds it:
   - Lines 1–5: one row per person
   - Lines 6–9: counts clicks
   - Lines 10–13: first report
   - Lines 14–15: clicked and then reported
3. Run it: `python3 campaign.py`.
4. Check it from the repository root: `./check m01l03-07`.

## Expected output

```text
clicked    4 of 10
submitted  2 of 10
reported   4 of 10
first report arrived 0:04:00 after sending
clicked, then reported it: dev
```

## How to check

`./check m01l03-07` copies `starter/` into a scratch directory and runs `python3 campaign.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
