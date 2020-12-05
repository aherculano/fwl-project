class FirewallUUID(object):
    def __init__(self, uuid: str):
        self.firewall_uuid = uuid

    @property
    def firewall_uuid(self):
        return self._firewall_uuid

    @firewall_uuid.setter
    def _firewall_uuid(self, value: str):
        self._firewall_uuid = value

    def __eq__(self, other) -> bool:
        if isinstance(other, FirewallUUID):
            return self.firewall_uuid.__eq__(other.firewall_uuid)
        return False
