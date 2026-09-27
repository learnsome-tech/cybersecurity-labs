# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l04 — Incident Roles, Escalation & Crisis Comm
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l04
# © LearnSome.tech
import tomllib
from datetime import datetime, timedelta
policy = tomllib.load(open("severity.toml", "rb"))
def page(sev, raised, answers):     # answers: who acknowledged, and when
    level = policy[sev]
    wait = timedelta(minutes=level["escalate_after_min"])
    print(f"{raised:%H:%M} {sev}: {level['means']}")
    for step, who in enumerate(level["chain"]):
        paged = raised + step * wait
        print(f"  {paged:%H:%M} page {who}")
        ack = answers.get(who)
        if ack and ack < paged + wait:
            print(f"  {ack:%H:%M} acknowledged by {who}")
            print(f"  comms: {level['comms']}")
            return
    print("  nobody acknowledged and the chain has run out")
night = datetime(2026, 3, 14, 2, 14)
page("sev1", night, {"incident commander": night + timedelta(minutes=8)})
page("sev3", night, {})
