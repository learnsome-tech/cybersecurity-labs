# m05l02 · Disaster Recovery Sites: Hot, Warm & Cold

Module 5: Resilience & Disaster Recovery · lesson 5.2 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m05l02)

**Goal:** You can choose between hot, warm and cold recovery sites by working out their real recovery time and data loss against a system's RTO and RPO, and plan how to test the choice.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l02-02](m05l02-02/) | Would each site meet a six hour RTO? | Graded |
| [m05l02-03](m05l02-03/) | Synchronous versus asynchronous replication | Graded |
| [m05l02-05](m05l02-05/) | What distance does to every commit | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Break the plans on purpose

1. In site_fit.py find the LINK_GBPS at which the warm site just meets the six hour RTO.
2. Set DATA_TB to 20 and predict which plans still meet the RTO before running it.
3. In replicate.py ship to the async replica every four minutes; predict the orders lost.
4. Add your own office and recovery site to latency.py and read the round-trip floor.

> **Hint:** Warm meets six hours only if the copy takes two hours or less; orders arrive on even minutes.

## Check yourself

- The warm site had servers ready but still missed a six hour RTO. What made it late, and what would you change first?
- Why did the asynchronous replica lose exactly three orders when the primary failed at 14:37?
- A team wants synchronous replication from London to a site in Virginia. What would every write experience, and why?
- Which kind of test proves the DNS change, certificates and firewall rules at the recovery site, and why can a tabletop not prove it?
- Both sites use the same cloud account, identity provider and software build. What kind of event can take out both anyway?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
