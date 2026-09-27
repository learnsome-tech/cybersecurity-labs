# Exercises — Backup Architectures: 3-2-1, Immutability & Air-Gaps

Lesson `m05l03` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l03)

## Exercise 1: Attack and defend the backups

1. In backup_types.py add a Friday (13th) edit of logo.png; predict both Friday archives.
2. Change readonly.py so the attacker calls os.chmod and overwrites in place instead.
3. In verify.py rewrite manifest.json after the tamper; explain why the check now passes.
4. List your real backups against 3-2-1-1-0 and mark any copy an admin login can delete.

> **Hint**: A differential grows until the next full; deleting needs write access on the folder, not the file.


---

© LearnSome.tech · support@iwantto.learnsome.tech
