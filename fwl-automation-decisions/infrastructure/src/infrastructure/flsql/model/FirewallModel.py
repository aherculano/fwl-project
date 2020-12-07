class FirewallModel(object):
    # ORM
    id: int = None

    def __init__(self, name: str, uuid: str, access_layer: str):
        self.name = name
        self.uuid = uuid
        self.access_layer = access_layer

    def __repr__(self):
        return "<Firewall uuid={self.uuid}; name={self.name}; description={self.access_layer}>".format(self=self)
