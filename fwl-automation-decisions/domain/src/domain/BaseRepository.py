from abc import ABC, abstractmethod


class BaseRepository(ABC):

    @abstractmethod
    def add(self, o: object) -> object:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> [object]:
        raise NotImplementedError

    @abstractmethod
    def get(self, o: object) -> object:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: object) -> object:
        raise NotImplementedError
