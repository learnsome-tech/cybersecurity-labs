# Exercises — Security Architecture Gap Analysis

Lesson `m06l01` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l01)

## Exercise 1: Extend the gap check

1. Add 3389 to TARGET, allowed only from 10.20.9.0/24. Predict the new lines, then run it.
2. Change the temp debug source to 10.20.9.15/32. Predict whether that line is now met.
3. Add an Ipv6Ranges list with {"CidrIpv6": "::/0"} to the bastion rule. Is it reported?
4. Make the checker read Ipv6Ranges too, and report any IPv6 source as a gap.

> **Hint**: IPv6 sources sit in perm.get("Ipv6Ranges", []) under CidrIpv6. subnet_of across IP versions raises TypeError.


---

© LearnSome.tech · support@iwantto.learnsome.tech
