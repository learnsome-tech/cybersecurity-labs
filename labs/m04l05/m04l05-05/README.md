# m04l05-05 · Egress monitoring from Zeek connection logs

**Lesson:** [Data Loss Prevention & Egress Monitoring](https://learnsome.tech/learn/cybersecurity-course/m04l05) (lesson 4.5, module 4: Data Protection & Privacy) · Pro  
**Check:** Graded

## Goal

You can explain how a DLP rule decides that outbound content is sensitive, tune it against false positives, and spot bulk exfiltration in connection logs.

In the lesson: Content inspection fails once data is encrypted, so you also watch volume. Zeek, the network monitor, writes a conn log with one line per connection, and orig bytes counts what the inside host sent. This program reads the fields header, as Zeek's own tools do, rather than guessing column positions. Zeek writes a dash when a field has no value. Only connections from a local host to a non local one count, because a copy to the internal file server is not leaving the site. Totals are grouped by source and destination. It flags any pair that sent more than a hundred megabytes and more than ten times what it received. The ordinary browsing host received far more than it sent. The video call is large both ways and passes. But one laptop sent almost one point two gigabytes to one address in two connections of about twenty minutes each, after three in the morning.

## Files

- [`starter/conn.log`](starter/conn.log)
- [`starter/egress.py`](starter/egress.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m04l05/m04l05-05/starter`
2. Read `egress.py` the way the lesson builds it:
   - Lines 1–8: reads the fields header
   - Lines 9–11: a dash
   - Lines 12–18: leaving the site
   - Lines 19–22: flags any pair
3. Run it: `python3 egress.py`.
4. Check it from the repository root: `./check m04l05-05`.

## Expected output

```text
192.0.2.14 -> 198.51.100.7   sent     0.1 MB, received   27.7 MB
192.0.2.23 -> 203.0.113.50   sent  1210.1 MB, received    0.4 MB review
192.0.2.31 -> 198.51.100.20  sent   251.4 MB, received  239.8 MB
192.0.2.40 -> 198.51.100.53  sent     0.0 MB, received    0.0 MB
```

## How to check

`./check m04l05-05` copies `starter/` into a scratch directory and runs `python3 egress.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m04l05) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
