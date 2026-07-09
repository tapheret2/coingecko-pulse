from __future__ import annotations

from typing import Any

import httpx

BASE = "https://api.coingecko.com/api/v3"
UA = "coingecko-pulse/0.1 (educational; +https://github.com/tapheret2/coingecko-pulse)"


class CoinGecko:
    def __init__(self) -> None:
        self._c = httpx.Client(
            base_url=BASE,
            timeout=30,
            headers={"User-Agent": UA, "Accept": "application/json"},
        )

    def close(self) -> None:
        self._c.close()

    def __enter__(self) -> "CoinGecko":
        return self

    def __exit__(self, *a: object) -> None:
        self.close()

    def markets(self, n: int = 20, vs: str = "usd") -> list[dict[str, Any]]:
        r = self._c.get(
            "/coins/markets",
            params={
                "vs_currency": vs,
                "order": "market_cap_desc",
                "per_page": n,
                "page": 1,
                "sparkline": "false",
                "price_change_percentage": "24h",
            },
        )
        r.raise_for_status()
        return r.json()

    def simple_price(self, ids: list[str], vs: str = "usd") -> dict[str, Any]:
        r = self._c.get(
            "/simple/price",
            params={
                "ids": ",".join(ids),
                "vs_currencies": vs,
                "include_24hr_change": "true",
                "include_market_cap": "true",
            },
        )
        r.raise_for_status()
        return r.json()


def normalize_symbol(symbol: str) -> str:
    """Normalize user coin symbols (e.g. btc -> bitcoin is NOT done; just case)."""
    return (symbol or "").strip().lower()
