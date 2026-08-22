from admin import is_authorized, summarize_catalog


def test_is_authorized_no_token_configured(monkeypatch):
    monkeypatch.delenv("ADMIN_TOKEN", raising=False)
    assert is_authorized("anything") is True


def test_is_authorized_correct_token(monkeypatch):
    monkeypatch.setenv("ADMIN_TOKEN", "secret123")
    assert is_authorized("secret123") is True
    assert is_authorized("wrong") is False


def test_summarize_catalog():
    products = [{"price": 10.0}, {"price": 20.0}]
    summary = summarize_catalog(products)
    assert summary["total_products"] == 2
    assert summary["total_value"] == 30.0
