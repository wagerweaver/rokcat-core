from review_logger import ReviewLogger
from log_schema import format_log
from sheets_logger import SheetsLogger

logger = ReviewLogger([
    SheetsLogger("creds.json", "ROKCAT_Trades")
])

log_entry = format_log(
    "Trade Executed", "2025-03-28", "USDC", "MEXC→Uniswap", 1.24, 0.19, "Win", "Spread held"
)

logger.log(log_entry)
