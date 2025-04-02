# 🔁 Triplet Scanner

This module enables ROKCAT to discover multi-hop arbitrage chains across three tokens or exchanges (A → B → C). It maps eligible routes from live token pairs, applies validation rules, and scores viable opportunities for execution prioritization.

The goal is to identify profitable paths missed by basic two-leg spread detectors — powering ROKCAT’s opportunity intelligence layer.

## 📂 Key Files

- `triplet_scanner.py` — Main orchestrator for route generation
- `route_validator.py` — Ensures path viability (spread, liquidity, token/chain match)
- `route_scorer.py` — Composite scoring logic (spread, fees, reliability)
- `patterns.py` — Triplet pattern generator from token pair graph
- `models.py` — ScanResult and route object structures
- `utils.py` — Misc helpers for formatting, math, and edge case logic
- `tests/` — Unit test harness (`test_triplet_scanner.py`)

## 📄 References

- [Triplet Scanner — Technical Execution Guide] https://docs.google.com/document/d/1F-V8uUKUNJmsH-sX7h9DjX_SM93JL6GLAhD3lecbqJs/edit?usp=sharing  
  _Logic architecture, filtering rules, and system integration plan_

- [Triplet Scanner — Implementation Blueprint] https://docs.google.com/document/d/1kE7NMYb6JWcPN5L9enxDlUY-gNjZz56OlxgFU_XnfOk/edit?usp=sharing 
  _Module file map, class references, and extensibility roadmap_

---
