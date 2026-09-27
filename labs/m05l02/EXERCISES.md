# Exercises — Disaster Recovery Sites: Hot, Warm & Cold

Lesson `m05l02` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l02)

## Exercise 1: Break the plans on purpose

1. In site_fit.py find the LINK_GBPS at which the warm site just meets the six hour RTO.
2. Set DATA_TB to 20 and predict which plans still meet the RTO before running it.
3. In replicate.py ship to the async replica every four minutes; predict the orders lost.
4. Add your own office and recovery site to latency.py and read the round-trip floor.

> **Hint**: Warm meets six hours only if the copy takes two hours or less; orders arrive on even minutes.


---

© LearnSome.tech · support@iwantto.learnsome.tech
