class FirewallName(object):

    def __init__(self, value: str):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value.strip().upper()

    def __eq__(self, other) -> bool:
        if isinstance(other, FirewallName):
            return self.value.__eq__(other.value)
        return False
