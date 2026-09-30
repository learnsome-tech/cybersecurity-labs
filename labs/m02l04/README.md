# m02l04 · Regulatory Compliance: SOC 2, HIPAA, GDPR & PCI-DSS

Module 2: Governance, Risk & Compliance · lesson 2.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m02l04)

**Goal:** You can tell which of SOC 2, HIPAA, GDPR and PCI DSS applies and why, find card data that has leaked into scope, and work out the breach notification deadlines one incident triggers.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l04-03](m02l04-03/) | Finding card numbers in a support export | Graded |
| [m02l04-04](m02l04-04/) | Why PCI DSS wants keyed hashes | Graded |
| [m02l04-06](m02l04-06/) | One incident, several notification clocks | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Test the scanner and the clocks

1. Add a ticket with a card number typed as 4111-1111-1111-1111. Predict, then run pan_scan.py.
2. Change one digit of 5555555555554444 in the log. What does the Luhn check report now?
3. In breach_clock.py set US-CA to 450. Predict which HIPAA lines change, then run it.

> **Hint:** The HHS threshold counts everyone affected; the media threshold counts residents of one state.

## Check yourself

- Customers sometimes paste card numbers into a support chat that is saved in the ticketing system. What does that do to PCI DSS scope, and what is the better fix?
- Why could the attacker recover the card number from a plain SHA-256 hash stored next to the masked number?
- A breach affects 620 patients in California and 140 in Texas. Which HIPAA notifications does it trigger?
- A vendor gives you a SOC 2 Type I report. What can it not tell you?
- PCI DSS is not a law. Why can a merchant still be penalised for ignoring it?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
