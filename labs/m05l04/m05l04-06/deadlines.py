# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l04 — Incident Roles, Escalation & Crisis Comm
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l04
# © LearnSome.tech
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

berlin, utc = ZoneInfo("Europe/Berlin"), ZoneInfo("UTC")
aware = datetime(2026, 10, 23, 16, 30, tzinfo=berlin)   # breach confirmed
clocks = {"NIS2 early warning": 24, "NIS2 notification": 72,
          "GDPR Art. 33 notice": 72}

print(f"{'became aware':19} {aware:%a %d %b %H:%M %Z}")
for name, hours in clocks.items():
    due = (aware.astimezone(utc) + timedelta(hours=hours)).astimezone(berlin)
    wall = aware + timedelta(hours=hours)   # adds hours to the wall clock
    print(f"{name:19} {due:%a %d %b %H:%M %Z}  wall-clock sum: {wall:%H:%M}")
