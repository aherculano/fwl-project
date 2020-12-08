class Criticality(object):

    def __init__(self, value: int):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value
        if value > 4 or value < 0:
            raise ValueError("Invalid Criticality Value: {value}".format(value))

    def __eq__(self, other):
        if isinstance(other, Criticality):
            return self.value == other.value
        return False
