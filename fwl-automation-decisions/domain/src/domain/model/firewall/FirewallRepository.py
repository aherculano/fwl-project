from abc import ABC, abstractmethod

from domain.BaseRepository import BaseRepository
from .Firewall import Firewall
from .FirewallUUID import FirewallUUID


class FirewallRepository(BaseRepository, ABC):

    @abstractmethod
    def add(self, o: Firewall) -> Firewall:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> [Firewall]:
        raise NotImplementedError

    @abstractmethod
    def get(self, o: Firewall) -> Firewall:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: FirewallUUID) -> Firewall:
        raise NotImplementedError

    @abstractmethod
    def exists(self, id: FirewallUUID) -> bool:
        raise NotImplementedError
