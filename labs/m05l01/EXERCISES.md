# Exercises — Business Impact Analysis, RTO & RPO Modeling

Lesson `m05l01` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l01)

## Exercise 1: Change the inputs, predict, then run

1. Add an email row to bia.csv that depends on identity; predict its ready time, then run.
2. Set identity's restore_h to 1 and predict which late verdict disappears.
3. In rpo_demo.py set EVERY to one hour and predict how many orders are lost.
4. In availability.py double only the database; which part now limits you?

> **Hint**: Ready time is your own restore plus the slowest dependency; worst-case loss is one backup interval.


---

© LearnSome.tech · support@iwantto.learnsome.tech
