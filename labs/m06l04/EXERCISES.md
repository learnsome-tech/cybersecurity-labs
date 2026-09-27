# Exercises — Security Capstone Review & Certification

Lesson `m06l04` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l04)

## Exercise 1: Finish the review yourself

1. Make a new cert.pem with openssl req -x509 and an RSA 2048 key; rerun inspect_cert.sh.
2. Delete one snapshot from snapshots.json. Predict the worst case, then run backup_rpo.py.
3. Set AUDIT to 2026-10-02T09:00:00+00:00 and explain the extra line it prints.
4. Add both findings to register.csv from lesson two and run register_review.py.

> **Hint**: openssl req -x509 -newkey rsa:2048 -nodes -keyout key.pem -out cert.pem -days 365 -subj /CN=booking.example.org


---

© LearnSome.tech · support@iwantto.learnsome.tech
