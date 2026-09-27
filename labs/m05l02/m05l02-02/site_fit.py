# Cybersecurity Fundamentals, GRC & Cryptography — lesson m05l02 — Disaster Recovery Sites: Hot, Warm & Cold
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m05l02
# © LearnSome.tech
RTO_H = 6            # checkout, from the business impact analysis
DATA_TB = 2          # newest backup set that must reach the site
LINK_GBPS = 1        # bandwidth into the recovery site

copy_h = DATA_TB * 8000 / LINK_GBPS / 3600    # terabytes to gigabits

plans = {
    "cold": {"deliver and rack hardware": 72, "build servers": 12,
             "copy backups in": copy_h, "test and cut over": 2},
    "warm": {"power on and patch": 2, "copy backups in": copy_h,
             "test and cut over": 2},
    "hot":  {"replica already current": 0, "switch DNS and test": 0.5},
}
for site, steps in plans.items():
    total = sum(steps.values())
    verdict = "meets" if total <= RTO_H else "misses"
    slowest = max(steps, key=steps.get)
    print(f"{site:4} {total:5.1f}h  {verdict} RTO {RTO_H}h, slowest: {slowest}")
