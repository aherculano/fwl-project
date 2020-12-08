from abc import ABC, abstractmethod

from domain.model.zone_connection import ZoneConnection

from .ZoneConnectionDTO import ZoneConnectionDTO


class ZoneConnectionMapper(ABC):

    @abstractmethod
    def dto2domain(self, dto: ZoneConnectionDTO) -> ZoneConnection:
        raise NotImplementedError

    @abstractmethod
    def domain2dto(self, dom: ZoneConnection) -> ZoneConnectionDTO:
        raise NotImplementedError
