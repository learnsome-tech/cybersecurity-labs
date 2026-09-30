# m02l03 · Security Frameworks: NIST CSF 2.0, ISO 27001 & CIS

Module 2: Governance, Risk & Compliance · lesson 2.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m02l03)

**Goal:** You can explain how NIST CSF 2.0, ISO 27001 and the CIS Controls differ, use a crosswalk to find evidence gaps across all three, and test a Kubernetes pod against the restricted Pod Security Standard.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m02l03-04](m02l03-04/) | One crosswalk, three frameworks, four gaps | Graded |
| [m02l03-06](m02l03-06/) | Testing a pod manifest against the restricted profile | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Close the gaps and harden the sidecar

1. Add PR.AT-01 evidence dated 2026-03-10 to evidence.csv. Predict the PR score, then run it.
2. Set MAX_AGE to 180 days. Predict which evidence goes stale before you run crosswalk.py.
3. Fix log-shipper in pod.json until check_pod.py says it meets restricted.
4. Add "privileged": true to the app container. Is it caught? If not, add the check.

> **Hint:** The restricted profile includes every baseline rule, and baseline forbids privileged containers.

## Check yourself

- A customer asks for your NIST CSF 2.0 certificate. Why can you not provide one, and what could you offer instead?
- Why did the crosswalk report a gap for PR.AT-01 even though training evidence was on file?
- Your ISO 27001 certificate is scoped to the payments platform. What does it tell a customer about your HR system?
- The pod set runAsNonRoot to true at pod level. Why did the log-shipper container still violate the restricted profile?
- Why is aiming for CSF Tier 4 (Adaptive) everywhere usually the wrong goal?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
