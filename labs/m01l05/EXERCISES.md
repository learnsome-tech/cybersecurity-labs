# Exercises — Security Governance vs Security Management

Lesson `m01l05` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l05)

## Exercise 1: Your turn: fix the evidence, not the paperwork

1. Change the drop-in to PasswordAuthentication no. Predict the checker's output first
2. Rename the drop-in to 99-cloud-init.conf with yes in it. Does the result change? Why?
3. Add the rule permitemptypasswords must be no, leaving it out of both config files
4. Change AS_OF in exceptions.py to 2026-11-01 and predict which new problem appears

> **Hint**: A keyword that appears in neither file falls back to sshd's built-in default, which the checker reports as unset.


---

© LearnSome.tech · support@iwantto.learnsome.tech
