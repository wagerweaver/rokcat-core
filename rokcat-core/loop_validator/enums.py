
from enum import Enum

class ValidationDecision(Enum):
    PROCEED = "proceed"
    MANUAL_REVIEW = "manual"
    HALT = "halt"
