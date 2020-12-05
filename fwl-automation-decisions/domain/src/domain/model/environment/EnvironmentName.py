class EnvironmentName(object):

    # TODO : VALIDATION
    def __init__(self, environment_name: str):
        self.value = environment_name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val: str):
        self._value = val.strip().upper()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, EnvironmentName):
            return self.value.__eq__(o.value)
        return False
