"""Bank of Communications public product endpoint research adapter.

Research-only: no automated requests are made. Enable collection only after
confirming official host, permitted access, request contract and field semantics.
Screenshot-sourced endpoint hints are not validated API documentation.
"""
SOURCE_ID = "bankcomm"
SOURCE_HOME = "https://www.bankcomm.com/"
CATALOG_PATH = "/SITE/queryJylcProductInfo.do"
NAV_PATH = "/SITE/queryJylcBreakDetail.do"

def collect():
    """Return no records until the public request contract is verified."""
    return []
