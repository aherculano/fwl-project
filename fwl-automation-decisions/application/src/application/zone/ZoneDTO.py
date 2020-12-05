from abc import ABC, abstractmethod


class ZoneDTO(ABC):

    @abstractmethod
    def to_dict(self):
        raise NotImplementedError
