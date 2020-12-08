from abc import ABC, abstractmethod

from ...BaseRepository import BaseRepository
from .ZoneConnection import ZoneConnection
from .ZonePair import ZonePair


class ZoneRepository(BaseRepository, ABC):

    @abstractmethod
    def add(self, o: ZoneConnection) -> ZoneConnection:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> [ZoneConnection]:
        raise NotImplementedError

    @abstractmethod
    def get(self, o: ZoneConnection) -> ZoneConnection:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: ZonePair) -> ZoneConnection:
        raise NotImplementedError

    @abstractmethod
    def exists(self, id: ZonePair) -> bool:
        raise NotImplementedError
