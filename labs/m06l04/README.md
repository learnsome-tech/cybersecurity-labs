# m06l04 · Security Capstone Review & Certification

Module 6: Enterprise Strategy & Audit · lesson 6.4 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m06l04)

**Goal:** You can gather certificate and backup evidence, test it against written targets, turn the gaps into owned register entries, and choose a sensible next certification.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m06l04-02](m06l04-02/) | Reading the certificate the service presents | Graded |
| [m06l04-03](m06l04-03/) | Measuring the real recovery point from backups | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Finish the review yourself

1. Make a new cert.pem with openssl req -x509 and an RSA 2048 key; rerun inspect_cert.sh.
2. Delete one snapshot from snapshots.json. Predict the worst case, then run backup_rpo.py.
3. Set AUDIT to 2026-10-02T09:00:00+00:00 and explain the extra line it prints.
4. Add both findings to register.csv from lesson two and run register_review.py.

> **Hint:** openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj /CN=booking.example.org

## Check yourself

- Why is a copy of the backup policy weaker evidence than the restic snapshot list?
- The backup program appends the review time to the list of snapshots. What would it miss without that line?
- The certificate is signed with SHA-256. Why is it still a finding?
- Of the two backup actions, why is adding an alert for failed jobs the more important one?
- A colleague plans to prepare for ISC2 CC using only this course. What will they still need to study elsewhere?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
