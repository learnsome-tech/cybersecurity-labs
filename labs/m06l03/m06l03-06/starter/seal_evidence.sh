#!/usr/bin/env bash
# Seal the evidence for control CHG-01 when testing is finished
sha256sum changes.csv sample.txt results.csv > manifest.sha256
cat manifest.sha256
sha256sum manifest.sha256    # this hash goes into the audit ticket

# Before the report is issued, someone quietly "tidies" one result
sed -i.bak 's/^CHG-1031,exception,.*/CHG-1031,pass,/' results.csv

sha256sum -c manifest.sha256
