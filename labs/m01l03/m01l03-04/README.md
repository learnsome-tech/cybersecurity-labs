# m01l03-04 · What the mail client did not show

**Lesson:** [Social Engineering, Phishing & Human Defense](https://learnsome.tech/learn/cybersecurity-course/m01l03) (lesson 1.3, module 1: Core Security Principles) · Free  
**Check:** Graded

## Goal

You can name the common attack vectors and social engineering techniques, read a suspicious email's raw headers and authentication results, spot lookalike domains, and judge a phishing awareness programme by how fast people report.

In the lesson: Python's standard email package parses the file the way a mail client does, so every header is available. parseaddr splits From into the display name and the address. Then the program prints Reply To, the Return Path, and each result in the Authentication Results header. Read the output. S P F passed, but only for the lookalike domain in the envelope. There is no D K I M signature at all. D M A R C failed, because no domain that passed a check lines up with example dot com in the From header. It failed and was still delivered, because the supplier publishes a policy of none, which asks receivers to report failures rather than block them. Their policy, not yours, decided. A policy of quarantine or reject would have stopped it at the gateway.

## Files

- [`starter/inspect_mail.py`](starter/inspect_mail.py): the listing from the lesson
- [`starter/invoice.eml`](starter/invoice.eml)
- [`expected.txt`](expected.txt): the output the check compares with
- [`check.json`](check.json): how `./check` runs and checks this lab

## Steps

1. Go to the starter: `cd labs/m01l03/m01l03-04/starter`
2. Read `inspect_mail.py` the way the lesson builds it:
   - Lines 1–6: email package parses
   - Lines 7–10: splits From
   - Lines 11–14: each result
3. Run it: `python3 inspect_mail.py`.
4. Check it from the repository root: `./check m01l03-04`.

## Expected output

```text
display name:  Dana Whitfield, Example Ltd Accounts
from address:  accounts@example.com
replies go to: accounts.example@mailbox.example.net
bounces go to: <billing@examp1e-pay.com>
auth result:   spf=pass smtp.mailfrom=examp1e-pay.com
auth result:   dkim=none
auth result:   dmarc=fail (p=none) header.from=example.com
```

## How to check

`./check m01l03-04` copies `starter/` into a scratch directory and runs `python3 inspect_mail.py` there, the way the site's lab sandbox does: that directory is the working directory and `HOME`, `LANG=C.UTF-8`, `TZ=UTC`, a limit of 10 seconds and 256 KiB of output per stream.

It passes when the output matches `expected.txt` by the site's rules, within the limits. Standard output is compared line by line; spaces at the end of a line and blank lines at the end do not count. If that differs, standard output followed by standard error is compared with Python traceback frames and blank lines set aside, so a lesson that shows an error passes when your program prints the same error. A pass here is a pass on the site.

---

[Open the lesson on LearnSome.tech](https://learnsome.tech/learn/cybersecurity-course/m01l03) · [All labs of this lesson](../README.md) · [Course README](../../../README.md)
