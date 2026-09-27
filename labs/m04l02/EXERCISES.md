# Exercises — Data States: Security at Rest, in Transit, and in Use

Lesson `m04l02` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l02)

## Exercise 1: Break and repair each state

1. In at-rest.sh, delete db.key right after encrypting. Predict what the restore step prints.
2. In tokens.py, add an order for card 4111111111111111 and predict its token before running.
3. In hashes.py, add a random salt kept beside the hash. Does the guess still succeed? Why?
4. Change wire.py to send JSON with a bearer token and confirm it is just as visible.

> **Hint**: A salt stored with the hash is public, so the attacker just adds it to each guess.


---

© LearnSome.tech · support@iwantto.learnsome.tech
