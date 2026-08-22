import json
import os
import urllib.request
import urllib.error


def fetch_products(catalog_url=None, api_key=None):
    catalog_url = catalog_url or os.environ.get("CATALOG_URL", "http://catalog:3000")
    api_key = api_key or os.environ.get("CATALOG_API_KEY", "")

    req = urllib.request.Request(
        f"{catalog_url}/products",
        headers={"X-API-Key": api_key},
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            return json.loads(response.read())
    except (urllib.error.URLError, urllib.error.HTTPError):
        return []


def is_authorized(token):
    """Logique pure, testée sans réseau : vérifie le jeton d'admin."""
    expected = os.environ.get("ADMIN_TOKEN", "")
    if not expected:
        return True
    return token == expected


def summarize_catalog(products):
    return {
        "total_products": len(products),
        "total_value": sum(p.get("price", 0) for p in products),
    }


if __name__ == "__main__":
    print("admin dashboard (stub) - would start an HTTP server here")
