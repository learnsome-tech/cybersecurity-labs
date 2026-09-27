# Exercises — Data Loss Prevention & Egress Monitoring

Lesson `m04l05` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l05)

## Exercise 1: Tune the rules

1. Add a Luhn-valid number that is really a gift card to outbound.eml. What would you change?
2. Send Mia's NI number and email base64-encoded through edm.py. Predict, then run.
3. Lower the egress threshold to 10 MB and decide whether each new flag is worth a ticket.
4. Add a DNS connection with orig_bytes of 40000000 and explain why that pattern matters.

> **Hint**: Card issuers have known prefixes; a rule can combine Luhn with an issuer range check.


---

© LearnSome.tech · support@iwantto.learnsome.tech
