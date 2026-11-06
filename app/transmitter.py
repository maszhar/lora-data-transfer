from transport.base import BaseTransport


class AppTransmitter:
    def __init__(self, transport: BaseTransport):
        self._transport = transport

    def send(self, message: str) -> bool:
        payload = message.encode("utf-8")
        print(f"[TRANSMITTER] Meminta pengiriman: {message}")
        return self._transport.send_bytes(payload)