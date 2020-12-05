class ZoneModel(object):
    # ORM
    id: int = None

    def __init__(self, name: str, env_id: int):
        self.name = name
        self.env_id = env_id

    def __repr__(self):
        return "<Zone name={self.name}; env_id={self.env_id}>".format(self=self)
