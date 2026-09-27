# Cybersecurity Fundamentals, GRC & Cryptography — lesson m01l01 — CIA Triad, Non-Repudiation & Parkerian Hexad
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m01l01
# © LearnSome.tech
import re

SSHD = re.compile(r"(Accepted|Failed) (\w+) for (?:invalid user )?(\S+) "
                  r"from (\S+)")
SUDO = re.compile(r"sudo:\s+(\S+) : (user NOT in sudoers ; )?"
                  r".*USER=(\S+) ; COMMAND=(.*)")
SHARED = {"deploy"}  # the whole team knows this password

for line in open("auth.log"):
    if m := SSHD.search(line):
        result, method, user, src = m.groups()
        what = f"authn {result.lower()} {method} from {src}"
    elif m := SUDO.search(line):
        user, refused, target, command = m.groups()
        verdict = "refused" if refused else "allowed"
        what = f"authz {verdict} as {target}: {command}"
    else:
        continue  # session lines, cron and the rest
    who = f"{user}?" if user in SHARED else user
    print(line[7:15], f"{who:<7}", what)
