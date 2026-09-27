# Cybersecurity Fundamentals, GRC & Cryptography — lesson m02l05 — Vendor & Third-Party Risk Management Programs
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m02l05
# © LearnSome.tech
import csv

SENSITIVE = {"employee_pii", "customer_pii", "cardholder", "security_logs"}
EVIDENCE = {
    1: "SOC 2 Type II or ISO 27001, SIG Core, pen test; yearly",
    2: "SIG Lite or CAIQ; every two years",
    3: "contract terms only; at renewal",
}

def tier(v):
    sensitive = v["data"] in SENSITIVE
    reach = v["access"] != "none"
    if sensitive and (reach or v["business_critical"] == "yes"):
        return 1
    return 2 if sensitive or reach else 3

for v in csv.DictReader(open("vendors.csv")):
    t = tier(v)
    print(f"{v['vendor']:17} tier {t}  {EVIDENCE[t]}")
