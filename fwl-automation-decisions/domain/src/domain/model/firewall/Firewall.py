from .FirewallName import FirewallName
from .FirewallUUID import FirewallUUID


class Firewall(object):

    def __init__(self, uuid: FirewallUUID, name: FirewallName, access_layer: str):
        self.uuid = uuid
        self.name = name
        self.access_layer = access_layer

    @property
    def uuid(self):
        return self._uuid

    @property
    def name(self):
        return self._name

    @property
    def access_layer(self):
        return self._access_layer

    @uuid.setter
    def uuid(self, value: str):
        self._uuid = value

    @name.setter
    def name(self, value: FirewallName):
        self._name = value

    @access_layer.setter
    def access_layer(self, value: str):
        self._access_layer = value

    def __eq__(self, other: object):
        if isinstance(other, Firewall):
            return self.uuid.__eq__(other.uuid)
        return False
