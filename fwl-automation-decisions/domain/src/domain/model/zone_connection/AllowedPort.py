class AllowedPort(object):
    def __init__(self, value: int):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: int):
        self._value = value

    def __eq__(self, other):
        if isinstance(other, AllowedPort):
            return self.value == other.value
        return False
