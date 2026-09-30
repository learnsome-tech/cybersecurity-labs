# m02l05 · Vendor & Third-Party Risk Management Programs

Module 2: Governance, Risk & Compliance · lesson 2.5 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m02l05)

**Goal:** You can tier vendors by the risk they bring, choose the evidence and contract terms each tier needs, check a vendor's SBOM against advisories, and verify their SLA with your own data.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l05-02](m02l05-02/) | Tiering vendors from the intake list | Graded |
| [m02l05-04](m02l05-04/) | Checking a vendor's SBOM against advisories | Graded |
| [m02l05-06](m02l05-06/) | Verifying an SLA from the vendor's own incident export | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Re-tier, re-check and re-price

1. Give Wingtip Surveys admin_sso access in vendors.csv. Predict its tier, then run tiering.py.
2. Set log4j-core to 2.17.1 and snakeyaml to 2.2 in the SBOM. Predict the output first.
3. Make degraded minutes count in sla.py. Work out the credit by hand, then run it.

> **Hint:** The credit table is checked from the lowest floor up, and the first floor you are under wins.

## Check yourself

- The printer vendor holds none of your data. Why did it still land in tier two?
- A vendor's questionnaire says all bundled software is patched, but its SBOM lists log4j-core 2.14.1. What does that tell you, and what do you do?
- Why does the SBOM check turn versions into integer tuples instead of comparing the strings?
- It is September and a vendor's latest SOC 2 Type II covers January to December last year. What should you ask for?
- Your team wants to run its own penetration test against a vendor's API. What must be agreed first?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
