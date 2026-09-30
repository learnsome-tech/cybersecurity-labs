# m06l01 · Security Architecture Gap Analysis

Module 6: Enterprise Strategy & Audit · lesson 6.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m06l01)

**Goal:** You can compare exported security configuration against a written target architecture, find the gaps with a script, and rank them for a plan.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l01-02](m06l01-02/) | The current state: exported security group rules | Read along |
| [m06l01-03](m06l01-03/) | Checking every rule against the target | Graded |
| [m06l01-04](m06l01-04/) | Private is not the same as allowed | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the gap check

1. Add 3389 to TARGET, allowed only from 10.20.9.0/24. Predict the new lines, then run it.
2. Change the temp debug source to 10.20.9.15/32. Predict whether that line is now met.
3. Add an Ipv6Ranges list with {"CidrIpv6": "::/0"} to the bastion rule. Is it reported?
4. Make the checker read Ipv6Ranges too, and report any IPv6 source as a gap.

> **Hint:** IPv6 sources sit in perm.get("Ipv6Ranges", []) under CidrIpv6. subnet_of across IP versions raises TypeError.

## Check yourself

- The architecture diagram shows the database reachable only from the app tier. Why is that not evidence of the current state?
- A reviewer marks a rule allowing port 5432 from 10.0.0.0/8 as met because the range is private. What did they test, and what should they have tested?
- Why did the migration rule on the database tier appear as an SSH gap when it never mentions port 22?
- The bastion rule allowing 0.0.0.0/0 is already blocked by a host firewall. What should happen to the gap?
- Why is 'databases are segmented' a poor target statement, and what would a testable version say?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
