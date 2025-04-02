class ReversionMonitor:
    def __init__(self, exit_threshold):
        self.exit_threshold = exit_threshold

    def should_exit(self, current_price, fair_value):
        reversion = (current_price - fair_value) / fair_value
        return reversion >= self.exit_threshold
