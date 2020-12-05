class EnvironmentModel(object):
    # ORM
    id: int = None

    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return "<DatacenterEnvironment name={self.name}>".format(self=self)
