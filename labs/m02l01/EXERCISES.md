# Exercises — Security Baselines, Policies & Hardening Standards

Lesson `m02l01` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l01)

## Exercise 1: Break and fix the SSH baseline yourself

1. Move the Include line to the end of sshd_config. Predict the audit result, then run audit.py.
2. Add 'maxsessions 5' to ssh_standard.txt. Guess what sshd uses when it is unset, then check.
3. In change.sh, back out CHG-2291 with git revert --no-edit HEAD and read the log again.

> **Hint**: For most keywords sshd keeps the first value it reads, and Include is read where it appears.


---

© LearnSome.tech · support@iwantto.learnsome.tech
