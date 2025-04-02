from discount_entry import DiscountBuyStrategy
from reversion_monitor import ReversionMonitor
from config import CONFIG

entry_logic = DiscountBuyStrategy(CONFIG)
exit_monitor = ReversionMonitor(CONFIG["exit_threshold"])

# Example inputs
price = 0.78
fair_value = 1.00
volume = 15000

if entry_logic.should_enter(price, fair_value, volume):
    print("✅ DISCOUNT BUY: Entered position")

    # Later...
    if exit_monitor.should_exit(1.05, fair_value):
        print("📤 EXIT TRIGGERED: Sell position")
