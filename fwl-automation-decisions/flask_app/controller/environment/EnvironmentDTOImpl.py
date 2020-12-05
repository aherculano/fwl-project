from application import EnvironmentDTO


class EnvironmentDTOImpl(EnvironmentDTO):

    def __init__(self, environment_name: str):
        self.environment_name = environment_name

    def to_dict(self) -> dict:
        return {
            "environment_name": self.environment_name
        }

    @staticmethod
    def from_dict(data: dict):
        env_name = data.get('environment_name')
        return EnvironmentDTOImpl(env_name)
