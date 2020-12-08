class AllowedPortModel:

    def __init__(self, port: int):
        self.port = port

    def __eq__(self, other):
        if isinstance(AllowedPortModel):
            return self.port == other.port
        return False
