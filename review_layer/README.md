# 📊 Review Layer

The Review Layer acts as ROKCAT’s internal telemetry and analytics engine — logging every trade decision, execution path, error event, and route score into structured formats for post-trade review and performance improvement.

This module supports logging to Google Sheets, Notion, and future time-series databases.

## 📂 Key Files

- `review_logger.py` — Core engine for structured logging
- `log_schema.py` — Unified log structure (timestamps, types, values)
- `sheets_logger.py` — Google Sheets writer and update handler
- `notion_logger.py` — Log streaming to Notion database views
- `integration_hook.py` — Drop-in reference for main ROKCAT pipeline
- `tests/` — Unit test harness (`test_review_layer.py`)

## 📄 References

- [Review Layer — Technical Execution Guide] https://docs.google.com/document/d/1MxJo5IYHmUAZehIhqTb_q-L0qaIhrdmCPAt4W-hs8nU/edit?usp=sharing
  _Real-time and post-trade logging, review workflows, export options_

- [Review Layer — Implementation Blueprint] https://docs.google.com/document/d/1q5RqMEjr7d52Ry0MqfBFc8w_e2sZeYmIhQGbju_biJY/edit?usp=sharing
  _Log schema definitions, Sheets/Notion setup, test hooks_

---
