import time
import threading
from typing import Callable, Optional
from transport.base import BaseTransport


class DummySocketTransport(BaseTransport):
    """Simulasi socket untuk keperluan pengembangan awal."""

    def __init__(self):
        self._on_receive_cb: Optional[Callable[[bytes], None]] = None
        self._running = False
        self._sim_thread: Optional[threading.Thread] = None

    def start(self) -> None:
        self._running = True
        self._sim_thread = threading.Thread(
            target=self._simulate_incoming_socket_data, daemon=True
        )
        self._sim_thread.start()

    def stop(self) -> None:
        self._running = False

    def send_bytes(self, data: bytes) -> bool:
        print(f" -> [SOCKET DUMMY] Data terkirim ke wire: {data}")
        return True

    def set_on_receive_callback(self, callback: Callable[[bytes], None]) -> None:
        self._on_receive_cb = callback

    def _simulate_incoming_socket_data(self) -> None:
        count = 0
        while self._running:
            time.sleep(2)
            count += 1
            if self._on_receive_cb:
                self._on_receive_cb(f"Paket data #{count} dari socket".encode("utf-8"))