from abc import ABC, abstractmethod

from domain.model.zone import Zone

from .ZoneDTO import ZoneDTO


class ZoneMapper(ABC):

    @abstractmethod
    def dto2domain(self, dto: ZoneDTO) -> Zone:
        raise NotImplementedError

    @abstractmethod
    def domain2dto(self, dom: Zone) -> ZoneDTO:
        raise NotImplementedError
