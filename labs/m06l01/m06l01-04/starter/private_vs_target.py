import ipaddress

target = ipaddress.ip_network("10.20.1.0/24")        # the app subnet
sources = ["10.20.1.0/24", "10.20.1.128/25", "10.20.2.0/24", "10.0.0.0/8",
           "0.0.0.0/0"]

for cidr in sources:
    net = ipaddress.ip_network(cidr)
    print(f"{cidr:15} private={net.is_private!s:5} "
          f"inside target={net.subnet_of(target)!s:5} "
          f"addresses={net.num_addresses}")
