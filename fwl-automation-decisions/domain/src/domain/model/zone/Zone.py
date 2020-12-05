from .ZoneName import ZoneName
from ..environment.EnvironmentName import EnvironmentName


class Zone(object):
    def __init__(self, zone_name: ZoneName, environment: EnvironmentName):
        self.zone_name = zone_name
        self.environment = environment

    @property
    def zone_name(self):
        return self._zone_name

    @property
    def environment(self):
        return self._environment

    @zone_name.setter
    def zone_name(self, value: ZoneName):
        self._zone_name = value

    @environment.setter
    def environment(self, value: EnvironmentName):
        self._environment = value

    def __eq__(self, other) -> bool:
        if type(other) is Zone:
            return self.zone_name.__eq__(other.zone_name)
        return False
