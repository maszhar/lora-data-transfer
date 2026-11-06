import time
import threading
from queue import Queue
from typing import Optional
from transport.base import BaseTransport


class AppReceiver:
    def __init__(self, transport: BaseTransport):
        self._transport = transport
        self._queue: Queue[bytes] = Queue()
        self._is_running = False
        self._worker_thread: Optional[threading.Thread] = None

        # Registrasi callback listener
        self._transport.set_on_receive_callback(self._handle_raw_data)

    def _handle_raw_data(self, data: bytes) -> None:
        """Callback 'on_receive' saat data mentah diterima dari transport."""
        self._queue.put(data)

    def start(self) -> None:
        self._is_running = True
        self._worker_thread = threading.Thread(target=self._process_queue, daemon=True)
        self._worker_thread.start()

    def _process_queue(self) -> None:
        """Loop terpisah untuk memproses queue data tanpa mengganggu socket."""
        while self._is_running:
            if not self._queue.empty():
                payload = self._queue.get()
                self._on_payload_processed(payload)
                self._queue.task_done()
            time.sleep(0.01)

    def _on_payload_processed(self, payload: bytes) -> None:
        """Logika aplikasi saat data selesai diproses."""
        decoded_text = payload.decode("utf-8", errors="ignore")
        print(f"[RECEIVER] Diterima & Diproses: {decoded_text}")

    def stop(self) -> None:
        self._is_running = False
        if self._worker_thread:
            self._worker_thread.join()