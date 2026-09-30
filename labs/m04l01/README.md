# m04l01 · Data Classification Schemes & Sensitivity Labeling

Module 4: Data Protection & Privacy · lesson 4.1 · Pro · [Open the lesson](https://learnsome.tech/learn/cybersecurity-course/m04l01)

**Goal:** You can choose a classification label for a dataset, store it where it survives copying, and enforce it where data is shared or stored.

## Labs

| Lab | What it is | Check |
| --- | --- | --- |
| [m04l01-03](m04l01-03/) | Where an Office document keeps its label | Read along |
| [m04l01-04](m04l01-04/) | Stamp a label, copy the file, read it back | Graded |
| [m04l01-05](m04l01-05/) | A sharing gate that reads the label | Graded |

## Exercises

Open exercises from the lesson, to try on your own. They have no answer files: work them out, and use the labs above as reference.

### Extend the gate

1. Save custom.xml, labels.py and gate.py in one folder and run gate.py.
2. Predict, then test: pricing.docx sent externally to eu-west-1.
3. Stamp a file as Secret, which is not in RULES, and confirm every request is blocked.
4. Zip a docx with no custom.xml part and make read_label return None, not crash.

> **Hint:** ZipFile.namelist() lists the parts; check for docProps/custom.xml before reading it.

## Check yourself

- A confidential file is copied out of the finance share and attached to an email. Why does a label stored in the file's metadata still protect it when a folder-based label would not?
- Staff names and salary bands are each labelled internal. What label should a report that joins them get, and why?
- In gate.py, a file labelled Secret arrives, but Secret is not in the rules table. What happens, and why is that the behaviour you want?
- Why does data sovereignty lead a company to pin confidential customer records to particular storage regions?
- A Q R code printed on a ticket encodes the passenger's name and booking reference. Why should a data discovery scan still classify it?

---

[Course README](../../README.md) · [Cybersecurity Fundamentals, GRC & Cryptography on LearnSome.tech](https://learnsome.tech/courses/cybersecurity-course)
