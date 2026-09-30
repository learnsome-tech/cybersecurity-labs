import csv, re
seen = {}  # mac -> (ip, hostname); a later lease for a mac replaces earlier
text = open("dhcpd.leases").read()
for ip, body in re.findall(r"lease (\S+) \{(.*?)\}", text, re.S):
    mac = re.search(r"hardware ethernet ([0-9a-f:]+);", body).group(1)
    host = re.search(r'client-hostname "([^"]*)";', body)
    seen[mac] = (ip, host.group(1) if host else "no hostname")

inventory = {row["mac"]: row for row in csv.DictReader(open("inventory.csv"))}
for mac, (ip, host) in seen.items():
    asset = inventory.get(mac)
    if asset is None:
        print(f"{ip} {host}: not in inventory, unmanaged device")
    elif asset["status"] == "disposed":
        print(f"{ip} {host}: recorded as disposed but online, recover it")
    else:
        print(f"{ip} {host}: ok, {asset['owner']}, {asset['classification']}")
for mac, asset in inventory.items():
    if asset["status"] == "assigned" and mac not in seen:
        print(f"{asset['asset_tag']}: assigned to {asset['owner']}, not seen")
