from carte import carte
from attributes_validator import is_valid_number
class mountain(carte):
    def __init__(self, axis_h, axis_v):
        self.axis_h=is_valid_number(axis_h)
        self.axis_v=is_valid_number(axis_v)
