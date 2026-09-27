# Exercises — Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS

Lesson `m02l03` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l03)

## Exercise 1: Close the gaps and harden the sidecar

1. Add PR.AT-01 evidence dated 2026-03-10 to evidence.csv. Predict the PR score, then run it.
2. Set MAX_AGE to 180 days. Predict which evidence goes stale before you run crosswalk.py.
3. Fix log-shipper in pod.json until check_pod.py says it meets restricted.
4. Add "privileged": true to the app container. Is it caught? If not, add the check.

> **Hint**: The restricted profile includes every baseline rule, and baseline forbids privileged containers.


---

© LearnSome.tech · support@iwantto.learnsome.tech
