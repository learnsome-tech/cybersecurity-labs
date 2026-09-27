#!/usr/bin/env bash
# Cybersecurity Fundamentals, GRC & Cryptography — lesson m06l03 — Internal Audits, Sampling & Evidence Chains
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l03
# © LearnSome.tech
# Seal the evidence for control CHG-01 when testing is finished
sha256sum changes.csv sample.txt results.csv > manifest.sha256
cat manifest.sha256
sha256sum manifest.sha256    # this hash goes into the audit ticket

# Before the report is issued, someone quietly "tidies" one result
sed -i.bak 's/^CHG-1031,exception,.*/CHG-1031,pass,/' results.csv

sha256sum -c manifest.sha256
