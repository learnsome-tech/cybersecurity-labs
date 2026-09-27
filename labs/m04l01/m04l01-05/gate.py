# Cybersecurity Fundamentals, GRC & Cryptography — lesson m04l01 — Data Classification Schemes & Sensitivity Labeling
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m04l01
# © LearnSome.tech
from labels import stamp, read_label
# label: (may leave the company?, storage regions allowed, None means any)
RULES = {"Public": (True, None), "Internal": (False, None),
         "Confidential": (False, {"eu-west-1", "eu-central-1"}),
         "Restricted": (False, {"eu-central-1"})}

def decide(path, external, region):
    label = read_label(path)
    may_leave, regions = RULES.get(label, (False, set()))
    if external and not may_leave:
        return label, "block: label forbids external sharing"
    if regions is not None and region not in regions:
        return label, f"block: {region} not allowed for {label}"
    return label, "allow"
for name, label in [("brochure", "Public"), ("pricing", "Confidential"),
                    ("board-minutes", "Restricted")]:
    stamp(f"{name}.docx", label)
for path, where, region in [("brochure.docx", "external", "us-east-1"),
                            ("pricing.docx", "internal", "eu-west-1"),
                            ("pricing.docx", "internal", "us-east-1"),
                            ("board-minutes.docx", "external", "eu-central-1")]:
    print(path, where, region, *decide(path, where == "external", region))
