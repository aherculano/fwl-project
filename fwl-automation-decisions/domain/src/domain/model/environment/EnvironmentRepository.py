from abc import ABC, abstractmethod
from .Environment import Environment
from .EnvironmentName import EnvironmentName
from ...BaseRepository import BaseRepository


class EnvironmentRepository(BaseRepository, ABC):

    @abstractmethod
    def add(self, o: Environment) -> Environment:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> [Environment]:
        raise NotImplementedError

    @abstractmethod
    def get(self, o: Environment) -> Environment:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: EnvironmentName) -> Environment:
        raise NotImplementedError

    @abstractmethod
    def exists(self, id: EnvironmentName) -> bool:
        raise NotImplementedError
