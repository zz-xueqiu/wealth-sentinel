"""Quality gates for normalized snapshot. Stdlib only."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    data = json.loads((ROOT / "data/products.json").read_text(encoding="utf-8"))
    products = data.get("products")
    if not isinstance(products, list):
        raise ValueError("products must be an array")
    seen = set()
    for p in products:
        if not isinstance(p, dict) or not p.get("code") or not p.get("name"):
            raise ValueError("product missing identity")
        key = (p.get("source"), p["code"], p["name"])
        if key in seen:
            raise ValueError("duplicate record: " + str(key))
        seen.add(key)
        if p.get("sale_status") not in ("unknown", "on_sale", "suspended", "closed", "matured"):
            raise ValueError("invalid sale_status")
        if p.get("verified") is not True and p.get("sale_status") == "on_sale":
            raise ValueError("unverified product cannot be on_sale")
    print(f"PASS: {len(products)} records; verified={sum(p.get('verified') is True for p in products)}")
if __name__ == "__main__":
    main()
