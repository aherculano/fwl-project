class FirewallModel(object):
    # ORM
    id: int = None

    def __init__(self, name: str, uuid: str, description: str):
        self.name = name
        self.uuid = uuid
        self.description = description

    def __repr__(self):
        return "<Firewall uuid={self.uuid}; name={self.name}; description={self.description}>".format(self=self)
