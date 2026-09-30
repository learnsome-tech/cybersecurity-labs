import configparser
import ipaddress
import sys
from datetime import timedelta
from failures import failures

jail = configparser.ConfigParser()
jail.read(sys.argv[1])
sshd = jail["sshd"]  # inherits every setting from [DEFAULT]
window = timedelta(minutes=int(sshd["findtime"].removesuffix("m")))
limit = sshd.getint("maxretry")
nets = sshd["ignoreip"].split()
ignored = [ipaddress.ip_network(n, strict=False) for n in nets]

for ip, times in failures.items():
    if any(ipaddress.ip_address(ip) in net for net in ignored):
        print(f"{ip:<14} never banned: inside ignoreip")
        continue
    runs = zip(times, times[limit - 1:])
    ban = next((end for start, end in runs if end - start <= window), None)
    print(f"{ip:<14}", f"banned at {ban:%H:%M:%S}" if ban else "not banned")
