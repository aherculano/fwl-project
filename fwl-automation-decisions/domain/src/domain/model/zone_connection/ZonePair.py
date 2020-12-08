from ..zone.ZoneName import ZoneName


class ZonePair(object):

    def __init__(self, source_zone: ZoneName, destination_zone: ZoneName):
        self.source_zone = source_zone
        self.destination_zone = destination_zone
        if self.source_zone.__eq__(self.destination_zone):
            raise ValueError("Invalid Zone Connection")

    @property
    def source_zone(self):
        return self._source_zone

    @source_zone.setter
    def source_zone(self, value: ZoneName):
        self._source_zone = value

    @property
    def destination_zone(self):
        return self._destination_zone

    @destination_zone.setter
    def destination_zone(self, value: ZoneName):
        self._destination_zone = value

    def get_pair_name(self):
        return self.source_zone.value + self.destination_zone.value

    def __eq__(self, other: object):
        if isinstance(other, ZonePair):
            return self.source_zone.__eq__(other.source_zone) and self.destination_zone.__eq__(other.destination_zone)
        return False
