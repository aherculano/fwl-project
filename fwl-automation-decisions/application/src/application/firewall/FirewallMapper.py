from abc import ABC, abstractmethod

from domain.model.firewall import Firewall
from .FirewallDTO import FirewallDTO


class FirewallMapper(ABC):

    @abstractmethod
    def dto2domain(self, dto: FirewallDTO) -> Firewall:
        raise NotImplementedError

    @abstractmethod
    def domain2dto(self, dom: Firewall) -> FirewallDTO:
        raise NotImplementedError
