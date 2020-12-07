from abc import ABC, abstractmethod


class FirewallDTO(ABC):

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError
