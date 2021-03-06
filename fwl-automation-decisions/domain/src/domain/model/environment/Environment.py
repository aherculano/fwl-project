from .EnvironmentName import EnvironmentName


class Environment(object):

    def __init__(self, environment_name: EnvironmentName):
        self.environment_name = environment_name

    @property
    def environment_name(self):
        return self._environment_name

    @environment_name.setter
    def environment_name(self, value: EnvironmentName):
        self._environment_name = value

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Environment):
            return o.environment_name.__eq__(self.environment_name)
        return False
