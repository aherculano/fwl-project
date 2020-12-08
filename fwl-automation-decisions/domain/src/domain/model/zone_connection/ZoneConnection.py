from .ZonePair import ZonePair
from .Criticality import Criticality
from .AllowedPort import AllowedPort
from ..firewall.FirewallUUID import FirewallUUID


class ZoneConnection(object):

    def __init__(self, zone_pair: ZonePair, criticality: Criticality, firewall_uuid: FirewallUUID, allowed_ports_list: [AllowedPort] = []):
        self.zone_pair = zone_pair
        self.criticality = criticality
        self.firewall_uuid = firewall_uuid
        self.allowed_ports_list = allowed_ports_list

    @property
    def zone_pair(self):
        return self._zone_pair

    @zone_pair.setter
    def zone_pair(self, value: ZonePair):
        self._zone_pair = value

    @property
    def criticality(self):
        return self._criticality

    @criticality.setter
    def criticality(self, value: Criticality):
        self._criticality = value

    @property
    def firewall_uuid(self):
        return self._firewall_uuid

    @firewall_uuid.setter
    def firewall_uuid(self, value: FirewallUUID):
        self._firewall_uuid = value

    @property
    def allowed_ports_list(self):
        return self._zone_pair

    @allowed_ports_list.setter
    def allowed_ports_list(self, value: [AllowedPort]):
        self._allowed_ports_list = value

    def __eq__(self, other):
        if isinstance(other, ZoneConnection):
            return self.zone_pair.__eq__(other.zone_pair)
        return False
