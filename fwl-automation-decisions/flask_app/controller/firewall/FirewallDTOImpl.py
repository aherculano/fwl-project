from application.firewall.FirewallDTO import FirewallDTO


class FirewallDTOImpl(FirewallDTO):

    def __init__(self, uuid: str, name: str, access_layer: str):
        self.uuid = uuid
        self.name = name
        self.access_layer = access_layer

    def to_dict(self) -> dict:
        return {
            "uuid": self.uuid,
            "name": self.name,
            "access_layer": self.access_layer
        }

    @staticmethod
    def from_dict(data: dict):
        return FirewallDTOImpl(data.get('uuid'), data.get('name'), data.get('access_layer'))
