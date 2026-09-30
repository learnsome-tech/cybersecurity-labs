# m01l03 · Social Engineering, Phishing & Human Defense

Module 1: Core Security Principles · lesson 1.3 · Free · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m01l03)

**Goal:** You can name the common attack vectors and social engineering techniques, read a suspicious email's raw headers and authentication results, spot lookalike domains, and judge a phishing awareness programme by how fast people report.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m01l03-03](m01l03-03/) | A business email compromise, raw | Read along |
| [m01l03-04](m01l03-04/) | What the mail client did not show | Graded |
| [m01l03-05](m01l03-05/) | Lookalike domains, as the machine sees them | Graded |
| [m01l03-07](m01l03-07/) | Scoring a phishing simulation | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Your turn: tune the email and the lookalikes

1. Change p=none to p=reject in invoice.eml. What should the gateway have done?
2. Add dkim=pass header.d=example.com and predict whether DMARC could pass
3. Add examp1e-invoices.com and a real domain of yours to SEEN; predict each line
4. In results.csv give dev no report. What does the last line print, and why worry?

> **Hint:** DMARC passes when either SPF or DKIM passes for a domain that aligns with the From domain.

## Check yourself

- The invoice email showed spf=pass. Why did that not make the message trustworthy?
- DMARC failed for example.com, yet the email still reached the inbox. Whose policy allowed that, and what would have stopped it?
- Why did the edit-distance check give example-invoices.com a high score, and what extra check would flag it?
- In the phishing simulation, why does the time to the first report matter more for limiting damage than the click rate?
- A colleague copies the full customer list to a USB stick the day after handing in their notice. Which kind of anomalous behaviour is that, and what should you do?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
