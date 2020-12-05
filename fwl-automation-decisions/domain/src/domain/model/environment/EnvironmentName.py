class EnvironmentName(object):

    # TODO : VALIDATION
    def __init__(self, environment_name: str):
        self.environment_name = environment_name

    @property
    def environment_name(self):
        return self._environment_name

    @environment_name.setter
    def environment_name(self, value: str):
        self._environment_name = value.strip().upper()

    def __eq__(self, o: object) -> bool:
        if type(o) is EnvironmentName:
            o: EnvironmentName
            return self.environment_name.__eq__(o.environment_name)
        return False
