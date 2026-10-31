"""Build a verified-aware snapshot without overwriting legacy products_data.json."""
import json
from pathlib import Path
from datetime import datetime, timezone
from normalize import dedupe
from chinawealth import collect as chinawealth_collect
from banks import collect as banks_collect

ROOT = Path(__file__).resolve().parents[1]
def read_json(path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return default

def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

def main():
    legacy = read_json(ROOT / "products_data.json", [])
    if not isinstance(legacy, list):
        raise ValueError("Legacy product file must be an array")
    rows = legacy + chinawealth_collect() + banks_collect()
    normalized = dedupe(rows)
    now = datetime.now(timezone.utc).isoformat()
    write_json(ROOT / "data/products.json", {
        "generated_at": now,
        "scope": "cash_management_daily_open_min_hold_1_30d_fixed_1_30d",
        "coverage_status": "incomplete",
        "products": normalized
    })
    write_json(ROOT / "data/sources.json", {
        "generated_at": now,
        "sources": [
            {"id": "legacy", "status": "unverified_seed"},
            {"id": "chinawealth", "status": "not_connected"},
            {"id": "banks", "status": "not_connected"}
        ]
    })
    print(f"Prepared {len(normalized)} unverified/verified records; no claim of live sale status.")

if __name__ == "__main__":
    main()
