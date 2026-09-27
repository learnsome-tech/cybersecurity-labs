# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l02 — Threat Actors, Motivations & Cyber Kill Chain
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l02
# © LearnSome.tech
import re
from collections import defaultdict

LINE = re.compile(r'(\S+) \S+ \S+ \[(.+?)\] "(\S+) (\S+) .*?" (\d{3})')
ABOUT_US = ("/about/", "/jobs/", "/suppliers")

visits = defaultdict(list)
for line in open("access.log"):
    ip, when, method, path, status = LINE.match(line).groups()
    visits[ip].append((method, path, status))

for ip, hits in visits.items():
    missing = sum(status == "404" for _, _, status in hits)
    about = sum(path.startswith(ABOUT_US) for _, path, _ in hits)
    logins = sum(method == "POST" for method, _, _ in hits)
    if missing == len(hits):
        kind = "opportunistic: asked only for software we do not run"
    elif about > 1 and logins:
        kind = "targeted: read up on our staff, then tried to log in"
    else:
        kind = "nothing unusual"
    print(f"{ip:<13} requests: {len(hits)}  {kind}")
