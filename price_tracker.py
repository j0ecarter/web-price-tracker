import argparse
import re
from pathlib import Path

from bs4 import BeautifulSoup


def parse_price(html: str, selector: str) -> float:
    # one selected price on the page
    soup = BeautifulSoup(html, "html.parser")
    element = soup.select_one(selector)
    if element is None:
        raise ValueError(f"No element matched selector: {selector}")
    match = re.search(r"(?:£|\$|€)?\s*([0-9][0-9,.]*)", element.get_text(" ", strip=True))
    if not match:
        raise ValueError("The selected element did not contain a price")
    number = match.group(1).replace(",", "")
    return float(number)


def should_alert(current_price: float, target_price: float) -> bool:
    return current_price <= target_price


def fetch_html(url: str) -> str:
    import requests

    response = requests.get(
        url,
        headers={"User-Agent": "PriceTrackerLearningProject/1.0"},
        timeout=15,
    )
    response.raise_for_status()
    return response.text


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare a page price with a target")
    parser.add_argument("--url", help="Optional live page URL")
    parser.add_argument("--selector", default="[data-price]")
    parser.add_argument("--target", type=float, default=80.00)
    args = parser.parse_args()

    html = fetch_html(args.url) if args.url else Path("data/demo_product.html").read_text(encoding="utf-8")
    price = parse_price(html, args.selector)
    print(f"Current price: £{price:.2f}")
    if should_alert(price, args.target):
        print(f"Price is at or below the £{args.target:.2f} target.")
    else:
        print(f"Price is still above the £{args.target:.2f} target.")


if __name__ == "__main__":
    main()
