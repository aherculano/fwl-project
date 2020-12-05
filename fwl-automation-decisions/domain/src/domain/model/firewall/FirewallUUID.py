class FirewallUUID(object):
    def __init__(self, uuid: str):
        self.value = uuid

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: str):
        self._value = value

    def __eq__(self, other) -> bool:
        if isinstance(other, FirewallUUID):
            return self.value.__eq__(other.value)
        return False
