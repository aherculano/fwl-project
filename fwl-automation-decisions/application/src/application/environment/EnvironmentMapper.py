from abc import ABC, abstractmethod

from domain.model.environment import Environment

from .EnvironmentDTO import EnvironmentDTO


class EnvironmentMapper(ABC):

    @abstractmethod
    def dto2domain(self, dto: EnvironmentDTO) -> Environment:
        raise NotImplementedError

    @abstractmethod
    def domain2dto(self, dom: Environment) -> EnvironmentDTO:
        raise NotImplementedError
