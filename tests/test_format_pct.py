from coingecko_pulse.client import format_pct, pick_fields

def test_format_pct():
    assert format_pct(1.234) == "+1.23%"
    assert format_pct(None) == "n/a"

def test_pick_fields():
    assert pick_fields({"id": "btc", "x": 1}, ["id", "missing"]) == {
        "id": "btc",
        "missing": None,
    }
