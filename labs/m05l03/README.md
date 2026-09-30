# m05l03 · Backup Architectures: 3-2-1, Immutability & Air-Gaps

Module 5: Resilience & Disaster Recovery · lesson 5.3 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m05l03)

**Goal:** You can design a backup scheme that survives ransomware, explaining incremental and differential chains, 3-2-1-1-0, immutability and air gaps, and prove a restore is intact.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m05l03-02](m05l03-02/) | Full, incremental and differential | Graded |
| [m05l03-04](m05l03-04/) | Read-only is not immutable | Graded |
| [m05l03-05](m05l03-05/) | Immutability enforced by the storage | Read along |
| [m05l03-07](m05l03-07/) | Zero errors: proving a restore is intact | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Attack and defend the backups

1. In backup_types.py add a Friday (13th) edit of logo.png; predict both Friday archives.
2. Change readonly.py so the attacker calls os.chmod and overwrites in place instead.
3. In verify.py rewrite manifest.json after the tamper; explain why the check now passes.
4. List your real backups against 3-2-1-1-0 and mark any copy an admin login can delete.

> **Hint:** A differential grows until the next full; deleting needs write access on the folder, not the file.

## Check yourself

- The backup file was read-only, yet the attacker deleted it. Which permission allowed that, and why?
- On Thursday, which archives does a restore need under the incremental scheme, and what happens if Wednesday's is corrupt?
- Why does a synchronous replica give no protection against ransomware encrypting the primary?
- An attacker holds an admin role that includes s3:BypassGovernanceRetention. Which Object Lock mode still protects your backups, and why?
- If the SHA-256 manifest is stored beside the backups with the same access, how can an attacker defeat the restore check?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
