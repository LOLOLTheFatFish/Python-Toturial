from enum import Enum

class State(Enum):
    INACRUVE = 0
    ACTIVE = 1
print(State.ACTIVE.value)