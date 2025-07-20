# 🤖 Pharos Testnet Bot - by YansDkk

Bot otomatis untuk Pharos Network Testnet. Bot ini akan:
- Melakukan login ke akun testnet Pharos
- Check-in harian otomatis
- Melakukan transaksi dummy (native token)
- Melakukan swap token WPHRS → USDC
- Menambahkan liquidity ke pool WPHRS/USDC

---

## ✨ Dibuat oleh: YansDkk

Bot ini dibangun untuk membantu pengguna aktif berpartisipasi dan mengumpulkan poin di testnet Pharos Network secara otomatis dan efisien.

---

## 🚀 Jalankan Otomatis di Gitpod

### 1. Buka di Gitpod:
Ganti `USERNAME` dan `REPO` dengan milikmu:
https://gitpod.io/#https://github.com/USERNAME/REPO
https://gitpod.io/#https://github.com/namauser/pharos-bot

### 2. Jalankan perintah setup:
```bash pip install -r requirements.txt python bot.py

📂Struktur File :
pharos-bot/
├── bot.py                # Bot utama otomatis swap, check-in, add LP
├── checkpoint.py         # Cek poin dan status user
├── config.py             # Konfigurasi alamat, ABI, RPC
├── privateKeys.txt       # List private key (tanpa spasi, 1 per baris)
├── proxy.txt             # (Opsional) list proxy
├── requirements.txt      # Dependency Python
└── README.md             # Dokumentasi project
