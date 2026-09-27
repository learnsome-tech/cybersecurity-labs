# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l04 — Defense-in-Depth & Security Control Categories
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l04
# © LearnSome.tech
import re
from collections import defaultdict
from datetime import datetime

FAILED = re.compile(r"^(\w+ +\d+ [\d:]+) .* Failed \w+ for .* from (\S+)")

failures = defaultdict(list)
for line in open("auth.log"):
    if m := FAILED.match(line):
        # syslog lines carry no year, so supply one
        stamp = datetime.strptime("2026 " + m[1], "%Y %b %d %H:%M:%S")
        failures[m[2]].append(stamp)

if __name__ == "__main__":
    for ip, times in failures.items():
        print(f"{ip:<14} {len(times)} failures",
              f"between {times[0]:%H:%M:%S} and {times[-1]:%H:%M:%S}")
