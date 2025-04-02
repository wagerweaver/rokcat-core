class DiscountBuyStrategy:
    def __init__(self, config):
        self.config = config

    def should_enter(self, price, fair_value, volume):
        discount = (fair_value - price) / fair_value
        if discount >= self.config["min_discount"] and volume >= self.config["min_volume"]:
            return True
        return False
