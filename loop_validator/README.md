# 🛡️ Loop Validator

This module acts as ROKCAT’s final pre-trade checkpoint — enforcing strict validation of arbitrage loops before capital is deployed. It evaluates spread, token compatibility, route viability, liquidity, and network status.

Returns one of three decision flags:  
- `PROCEED`  
- `HALT`  
- `MANUAL_REVIEW`

## 📂 Key Files

- `validator.py` — Core loop validation engine
- `config.py` — Slippage, spread, and liquidity thresholds
- `enums.py` — Decision flags used across the pipeline
- `errors.py` — Custom error classes for traceable failure states
- `cli.py` — Command-line tester for manual loop checks
- `integration_hook.py` — Sample usage inside a trade pipeline
- `sample_output.json` — Example structured validator output
- `tests/` — Unit test harness (`test_loop_validator.py`)

## 📄 References

- [Loop Validator — Technical Execution Guide] https://docs.google.com/document/d/1V3gbgCtpIuxgpx9Vl7qI5KvwSucZ1Avuu7brYErAqwo/edit?usp=sharing
  _Deep dive into logic, edge case handling, and module role in system_

- [Loop Validator — Implementation Blueprint] https://docs.google.com/document/d/1isd9s0RphAGM-HwkD1vTi46eBpHslZxCIKtuAATUC0I/edit?usp=sharing  
  _Code structure, integration hooks, and test setup notes_

---

