YEAR_MIN = 365 * 24 * 60

def avail(mtbf_h, mttr_h):          # share of time a part is working
    return mtbf_h / (mtbf_h + mttr_h)

def series(*parts):                 # every part must be up
    total = 1.0
    for a in parts:
        total *= a
    return total

def pair(a):                        # either of two copies will do
    return 1 - (1 - a) ** 2

web, db, power = avail(2000, 10), avail(8000, 8), avail(4000, 8)
designs = {"one of everything": series(web, db, power),
           "two web servers": series(pair(web), db, power),
           "two of everything": series(pair(web), pair(db), pair(power))}
for label, a in designs.items():
    down = (1 - a) * YEAR_MIN
    print(f"{label:18} {a:.4%}  down about {down:,.0f} min a year")
