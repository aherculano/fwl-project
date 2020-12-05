class FirewallAccessLayer(object):

    def __init__(self, access_layer: str):
        self.value = access_layer

    @property
    def value(self):
        return self._value

    @value.setter
    def _value(self, value: str):
        self._value = value

    def __eq__(self, other) -> bool:
        if isinstance(other, FirewallAccessLayer):
            return self.value.__eq__(other.value)
        return False
