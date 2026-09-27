# Cybersecurity Fundamentals, GRC & Cryptography — lesson m06l01 — Security Architecture Gap Analysis
# https://learnsome.tech/courses/cybersecurity-course/watch?lesson=m06l01
# © LearnSome.tech
import json
from ipaddress import ip_network

# Target state: port -> requirement id and the only sources allowed
TARGET = {5432: ("SEG-01", ["10.20.1.0/24"]),   # Postgres: app subnet
          22:   ("SEG-02", ["10.20.9.0/24"])}   # SSH: management subnet

def covers(perm, port):
    if perm["IpProtocol"] == "-1":              # -1 means all traffic
        return True
    return perm["FromPort"] <= port <= perm["ToPort"]

for group in json.load(open("sg.json"))["SecurityGroups"]:
    for perm in group["IpPermissions"]:
        for port, (req, allowed) in TARGET.items():
            if not covers(perm, port):
                continue
            for rng in perm["IpRanges"]:
                src = ip_network(rng["CidrIp"])
                ok = any(src.subnet_of(ip_network(a)) for a in allowed)
                print(req, group["GroupName"], port, src,
                      "met" if ok else "gap: " + rng["Description"])
