from abc import ABC, abstractmethod
from .Zone import Zone
from .ZoneName import ZoneName
from ...BaseRepository import BaseRepository


class ZoneRepository(BaseRepository, ABC):

    @abstractmethod
    def add(self, o: Zone) -> Zone:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> [Zone]:
        raise NotImplementedError

    @abstractmethod
    def get(self, o: Zone) -> Zone:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: ZoneName) -> Zone:
        raise NotImplementedError
