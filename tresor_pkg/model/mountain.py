from business.attributes_validator import is_valid_number
class mountain:
    def __init__(self, axis_h, axis_v):
        self.axis_h=axis_h
        self.axis_v=axis_v

    def is_valid_position(self):
        is_valid_number(self.axis_h)
        is_valid_number(self.axis_v)
