class ReviewLogger:
    def __init__(self, destinations):
        self.destinations = destinations  # list of output adapters

    def log(self, entry):
        for d in self.destinations:
            d.send(entry)
