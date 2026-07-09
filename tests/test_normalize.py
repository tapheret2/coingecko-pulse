from coingecko_pulse.client import normalize_symbol

def test_normalize_symbol():
    assert normalize_symbol(" BTC ") == "btc"
