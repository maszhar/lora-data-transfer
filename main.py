import time
from transport.dummy import DummySocketTransport
from app.receiver import AppReceiver
from app.transmitter import AppTransmitter

"""
Aplikasi dummy masih otomatis melakukan transmit dan receive dalam 1 fungsi main.
Logika ini harus dibenahi agar satu kali running hanya bisa transmit atau receive saja.

Transport belum mendukung streaming.
"""

def main():
    # 1. Inisialisasi Transport (Ganti ke RealSocketTransport saat tim konektivitas selesai)
    transport = DummySocketTransport()

    # 2. Inisialisasi App Receiver & Transmitter
    receiver = AppReceiver(transport)
    transmitter = AppTransmitter(transport)

    # 3. Jalankan Service
    transport.start()
    receiver.start()

    # 4. Tes Pengiriman Data
    transmitter.send("Halo dari Main App!")

    # Biarkan berjalan 5 detik untuk menerima data simulasi
    time.sleep(5)

    # 5. Shutdown Gracefully
    print("Menghentikan aplikasi...")
    receiver.stop()
    transport.stop()


if __name__ == "__main__":
    main()