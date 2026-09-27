# Exercises — Data Classification Schemes & Sensitivity Labeling

Lesson `m04l01` · [Watch](https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l01)

## Exercise 1: Extend the gate

1. Save custom.xml, labels.py and gate.py in one folder and run gate.py.
2. Predict, then test: pricing.docx sent externally to eu-west-1.
3. Stamp a file as Secret, which is not in RULES, and confirm every request is blocked.
4. Zip a docx with no custom.xml part and make read_label return None, not crash.

> **Hint**: ZipFile.namelist() lists the parts; check for docProps/custom.xml before reading it.


---

© LearnSome.tech · support@iwantto.learnsome.tech
