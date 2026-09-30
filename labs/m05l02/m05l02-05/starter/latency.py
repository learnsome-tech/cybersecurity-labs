from math import asin, cos, radians, sin, sqrt

SITES = {"Slough": (51.51, -0.60), "Manchester": (53.48, -2.24),
         "Frankfurt": (50.11, 8.68), "Ashburn": (39.04, -77.49)}
PRIMARY = (51.51, -0.13)            # London
FIBRE_KM_PER_MS = 200               # light in glass, about two thirds of c

def km(a, b):                       # great-circle distance, haversine
    (la1, lo1), (la2, lo2) = [map(radians, p) for p in (a, b)]
    h = sin((la2 - la1) / 2) ** 2 + \
        cos(la1) * cos(la2) * sin((lo2 - lo1) / 2) ** 2
    return 2 * 6371 * asin(sqrt(h))

for name, where in SITES.items():
    d = km(PRIMARY, where)
    rtt = 2 * d / FIBRE_KM_PER_MS   # a floor: real fibre routes are longer
    print(f"{name:10} {d:6,.0f} km  min RTT {rtt:5.1f} ms"
          f"  at most {1000 / rtt:6,.0f} commits/s per writer")
