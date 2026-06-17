from abc import ABC, abstractmethod
from typing import Any


class BaseRepository(ABC):

    @abstractmethod
    def save(self, item: Any) -> None:
        pass

    @abstractmethod
    def get_by_id(self, item_id: int):
        pass