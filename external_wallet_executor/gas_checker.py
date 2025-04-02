class GasChecker:
    def __init__(self, gas_thresholds):
        self.thresholds = gas_thresholds

    def is_ready(self, chain):
        current_gas = self.get_gas(chain)
        return current_gas >= self.thresholds.get(chain, 0)

    def get_gas(self, chain):
        # Placeholder: return mocked value
        return 80
