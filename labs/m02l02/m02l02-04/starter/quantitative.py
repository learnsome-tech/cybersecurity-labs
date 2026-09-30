import csv

def losses(av, ef, aro):
    sle = av * ef          # single loss expectancy: one event
    return sle, sle * aro  # annualised loss expectancy

with open("quant.csv", newline="") as f:
    for r in csv.DictReader(f):
        av, ef = float(r["asset_value"]), float(r["exposure_factor"])
        sle, before = losses(av, ef, float(r["aro"]))
        _, after = losses(av, ef, float(r["aro_with_control"]))
        cost = float(r["control_cost"])
        value = before - after - cost
        print(f'{r["id"]} {r["control"]}')
        print(f"   SLE {sle:,.0f}  ALE {before:,.0f} -> {after:,.0f}")
        print(f"   control {cost:,.0f} a year, net value {value:,.0f}")
