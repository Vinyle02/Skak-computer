from enum import Enum

class Color(Enum):
    WHITE = 0
    BLACK = 1
    
    def name(self):
        if self == Color.WHITE:
            return 'white'
        return 'black'