# m04l05 · Data Loss Prevention & Egress Monitoring

Module 4: Data Protection & Privacy · lesson 4.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m04l05)

**Goal:** You can explain how a DLP rule decides that outbound content is sensitive, tune it against false positives, and spot bulk exfiltration in connection logs.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l05-02](m04l05-02/) | The message the rule will inspect | Read along |
| [m04l05-03](m04l05-03/) | Pattern plus validation: finding card numbers | Graded |
| [m04l05-04](m04l05-04/) | Exact data match: fingerprints of your own records | Graded |
| [m04l05-05](m04l05-05/) | Egress monitoring from Zeek connection logs | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Tune the rules

1. Add a Luhn-valid number that is really a gift card to outbound.eml. What would you change?
2. Send Mia's NI number and email base64-encoded through edm.py. Predict, then run.
3. Lower the egress threshold to 10 MB and decide whether each new flag is worth a ticket.
4. Add a DNS connection with orig_bytes of 40000000 and explain why that pattern matters.

> **Hint:** Card issuers have known prefixes; a rule can combine Luhn with an issuer range check.

## Check yourself

- The card rule matched four sixteen-digit numbers in the email but reported only two as cards. What removed the other two, and why does that matter operationally?
- Why does exact data match catch the partner chat but ignore press@example.com, when a generic email pattern would flag both?
- Nearly all web traffic uses TLS. What does that mean for a network DLP sensor that does not decrypt, and which placement avoids the problem?
- In the Zeek conn.log, which evidence made 192.0.2.23 to 203.0.113.50 worth reviewing while the video call from 192.0.2.31 was not?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
