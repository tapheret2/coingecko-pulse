from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from coingecko_pulse.client import CoinGecko

app = typer.Typer(help="Crypto pulse via CoinGecko public API")
console = Console()


@app.command()
def top(n: int = 15, vs: str = "usd") -> None:
    with CoinGecko() as cg:
        rows = cg.markets(n=n, vs=vs)
    t = Table(title=f"Top {n} by market cap ({vs})")
    t.add_column("#")
    t.add_column("ID")
    t.add_column("Price")
    t.add_column("24h %")
    t.add_column("MCap")
    for i, r in enumerate(rows, 1):
        ch = r.get("price_change_percentage_24h") or 0
        style = "green" if ch >= 0 else "red"
        t.add_row(
            str(i),
            r.get("id", ""),
            f"{r.get('current_price')}",
            f"[{style}]{ch:+.2f}%[/{style}]",
            f"{r.get('market_cap')}",
        )
    console.print(t)


@app.command()
def price(ids: list[str] = typer.Argument(...)) -> None:
    with CoinGecko() as cg:
        data = cg.simple_price(ids)
    for k, v in data.items():
        ch = v.get("usd_24h_change") or 0
        console.print(f"{k}: ${v.get('usd')}  24h {ch:+.2f}%")


@app.command()
def snapshot(out: Path = typer.Option(Path("pulse.json"), "-o")) -> None:
    with CoinGecko() as cg:
        payload = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "markets": cg.markets(n=25),
        }
    out.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    console.print(f"wrote {out}")


if __name__ == "__main__":
    app()


def format_price(value: float, digits: int = 2) -> str:
    return f"${value:,.{digits}f}"


def format_pct(change: float, digits: int = 2) -> str:
    sign = "+" if change > 0 else ""
    return f"{sign}{change:.{digits}f}%"
