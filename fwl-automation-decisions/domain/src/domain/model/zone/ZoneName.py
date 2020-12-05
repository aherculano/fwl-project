class ZoneName(object):

    def __init__(self, zone_name: str):
        self.zone_name = zone_name

    @property
    def zone_name(self):
        return self._zone_name

    @zone_name.setter
    def _zone_name(self, value: str):
        self._zone_name = value.strip().upper()

    def __eq__(self, other) -> bool:
        if type(other) is ZoneName:
            return self.zone_name.__eq__(other.zone_name)
        return False
