# Web Price Tracker

I originally completed projects from Angela Yu's 100 Days of Code course across 2021–2023. After the original files were lost during a laptop change, this project was reconstructed in 2026 with substantial AI coding assistance. The Git history represents the reconstruction and first GitHub publication, not the original course timeline.

Extracts a price from HTML with a configurable CSS selector and compares it with a target. The included product page makes the default run fully offline.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python price_tracker.py
```

Live example: `python price_tracker.py --url https://example.com/product --selector '.price' --target 75`. Only use live mode on pages that permit automated requests. Run tests with `pytest`.
