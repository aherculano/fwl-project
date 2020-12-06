from application.zone.ZoneDTO import ZoneDTO


class ZoneDTOImpl(ZoneDTO):

    def __init__(self, zone_name: str, env_name: str):
        self.zone_name = zone_name
        self.environment_name = env_name

    def to_dict(self):
        return {
            "zone_name": self.zone_name,
            "environment_name": self.environment_name
        }

    @staticmethod
    def from_dict(data: dict):
        return ZoneDTOImpl(data.get("zone_name"), data.get("environment_name"))
