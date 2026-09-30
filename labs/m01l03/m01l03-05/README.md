# m01l03-05 · Lookalike domains, as the machine sees them

**Lesson:** [Social Engineering, Phishing & Human Defense](https://learnsome.tech/learn/cybersecurity-course/m01l03) (lesson 1.3, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can name the common attack vectors and social engineering techniques, read a suspicious email's raw headers and authentication results, spot lookalike domains, and judge a phishing awareness programme by how fast people report.

In the lesson: Now the domains. This list is the kind of thing a week of mail logs turns up. The second entry looks exactly like the real name, and on screen you cannot tell them apart. The distance function is a standard edit distance: how many single character changes turn one name into another. For each domain the program prints the form that really travels in D N S, using Python's I D N A codec, the edit distance from our domain, and the Unicode name of any character outside plain A S C I I. Run it. The second entry is not example dot com at all: its first letter is Cyrillic, and on the wire it becomes an x n dash dash name. The digit one and the r n pair are one and two edits away. The last entry keeps the whole brand, so distance misses it, and brand monitoring has to search for the name itself.

## Files

- [`starter/lookalike.py`](starter/lookalike.py): the listing from the lesson
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-05/starter`
2. Read `lookalike.py` the way the lesson builds it:
   - Lines 1–5: a week of mail logs
   - Lines 6–14: edit distance
   - Lines 15–19: For each domain
3. Run it: `python3 lookalike.py`.
4. Check it from the repository root: `./check m01l03-05`.

## Expected output

```text
example.com           edits: 0
xn--xample-2of.com    edits: 1  CYRILLIC SMALL LETTER IE
examp1e.com           edits: 1
exarnple.com          edits: 2
example-invoices.com  edits: 9
```

## How to check

`./check m01l03-05` copies `starter/` into a scratch directory and runs `python3 lookalike.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
