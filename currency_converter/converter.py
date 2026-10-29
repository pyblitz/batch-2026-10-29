"""Live currency converter. Tries the free open exchange-rate API, and falls
back to a built-in rates table (labelled with its date) if offline.
Run: python3 converter.py 100 USD PKR
"""
import json, sys, urllib.request

FALLBACK = {"USD": 1.0, "PKR": 280.0, "EUR": 0.92, "GBP": 0.79, "INR": 83.0}
FALLBACK_DATE = "2026-10-29 (built-in fallback table)"

def get_rates():
    try:
        with urllib.request.urlopen(
                "https://open.er-api.com/v6/latest/USD", timeout=8) as r:
            data = json.load(r)
        return data["rates"], "live API (open.er-api.com)"
    except Exception:
        return FALLBACK, FALLBACK_DATE

def convert(amount, frm, to):
    rates, source = get_rates()
    usd = amount / rates[frm.upper()]
    return usd * rates[to.upper()], source

if __name__ == "__main__":
    amount = float(sys.argv[1]) if len(sys.argv) > 1 else 100
    frm = sys.argv[2] if len(sys.argv) > 2 else "USD"
    to = sys.argv[3] if len(sys.argv) > 3 else "PKR"
    result, source = convert(amount, frm, to)
    print(f"{amount} {frm} = {result:.2f} {to}  (rates: {source})")
