"""Normalize disclosed products; never infer missing yields, status or redemption terms."""
from datetime import datetime, timezone

def normalize(row, source="legacy"):
    if not isinstance(row, dict):
        return None
    name = str(row.get("name") or "").strip()
    code = str(row.get("code") or "").strip()
    if not name or not code:
        return None
    kind = row.get("product_type") or "unverified"
    return {
        "code": code, "name": name,
        "issuer": row.get("issuer"),
        "product_type": kind,
        "short_term_category": row.get("short_term_category"),
        "sale_status": row.get("sale_status") or "unknown",
        "redemption_terms": row.get("redemption_terms"),
        "yield_7d": row.get("yield_7d"),
        "yield_7d_as_of": row.get("update_date"),
        "source": row.get("source") or source,
        "source_url": row.get("source_url"),
        "verified": bool(row.get("verified", False)),
    }

def dedupe(rows):
    result = {}
    for row in rows:
        item = normalize(row, row.get("source", "legacy") if isinstance(row, dict) else "legacy")
        if item:
            key = (item["source"], item["code"], item["name"])
            result[key] = item
    return sorted(result.values(), key=lambda x: (x["name"], x["code"]))
