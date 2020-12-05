from abc import abstractmethod, ABC


class EnvironmentDTO(ABC):

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError
