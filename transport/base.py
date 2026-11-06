from abc import ABC, abstractmethod
from typing import Callable


class BaseTransport(ABC):
    """Interface kontrak dasar untuk layer transport/socket."""

    @abstractmethod
    def start(self) -> None:
        pass

    @abstractmethod
    def stop(self) -> None:
        pass

    @abstractmethod
    def send_bytes(self, data: bytes) -> bool:
        pass

    @abstractmethod
    def set_on_receive_callback(self, callback: Callable[[bytes], None]) -> None:
        pass