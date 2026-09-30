import csv
from datetime import datetime

MONTH_MINUTES = 31 * 24 * 60                  # August
SLA, CREDITS = 99.9, [(99.0, 25), (99.9, 10)]  # from the MSA's SLA schedule

down = 0
for row in csv.DictReader(open("status_export_2026-08.csv")):
    start = datetime.fromisoformat(row["start"])
    mins = (datetime.fromisoformat(row["end"]) - start).total_seconds() / 60
    counted = row["kind"] == "outage"  # maintenance, degradation excluded
    down += mins if counted else 0
    print(f"{start:%d %b %H:%M} {row['kind']:11} {mins:3.0f} min", end="")
    print("  counted" if counted else "")

availability = 100 * (1 - down / MONTH_MINUTES)
credit = next((pct for floor, pct in CREDITS if availability < floor), 0)
allowed = MONTH_MINUTES * (100 - SLA) / 100
print(f"{down:.0f} min counted as down, {allowed:.1f} allowed")
print(f"availability {availability:.3f}%, credit due {credit}% of the fee")
