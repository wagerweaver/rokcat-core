class Triggers:
    @staticmethod
    def timeout(trade):
        return trade.execution_time > trade.config.max_execution_time

    @staticmethod
    def liquidity_drain(trade):
        return trade.sell_book_depth < trade.config.min_depth
