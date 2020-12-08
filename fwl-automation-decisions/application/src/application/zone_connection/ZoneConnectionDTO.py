from abc import ABC, abstractmethod


class ZoneConnectionDTO(ABC):
    @abstractmethod
    def to_dict(self):
        raise NotImplementedError
