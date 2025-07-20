# 🤖 Pharos Bot (Auto Check-in, Swap, LP)

Bot otomatis untuk melakukan check-in harian, swap token, add liquidity, dan native transaction di jaringan Pharos Testnet.  
Dibuat menggunakan Python & Web3.py dan bisa dijalankan dengan aman lewat Gitpod + GitHub

---

## 🧑‍💻 Dibuat oleh
By:YansDkk  
Telegram: [@zibrx](https://t.me/zibrx)

---

## ⚙️ Fitur Utama

- ✅ Auto check-in harian (Telegram)
- 🔁 Swap token otomatis
- 💧 Tambah liquidity otomatis
- ⛽ Kirim native token
- 🧅 Support proxy
- 🔐 Private key disembunyikan secara aman

---

## 🚀 Deploy via Gitpod (Step by Step)

### 1️⃣ Fork Repo ke GitHub

Klik tombol **Fork** di kanan atas untuk menyalin repo ini ke akun GitHub kamu.

---

### 2️⃣ Buka di Gitpod

Gantilah `USERNAME` dan `REPO` sesuai akun dan nama repo kamu:
```

[https://gitpod.io/#https://github.com/USERNAME/REPO](https://gitpod.io/#https://github.com/USERNAME/REPO)

````

---

### 3️⃣ Tambah Private Key ke Gitpod Secrets

1. Klik ikon **Settings (⚙️)** di kiri atas Gitpod
2. Masuk ke tab **"Secrets"**
3. Tambahkan secret baru:
   - **Name:** `PRIVATE_KEYS`
   - **Value:** `0xabc...,0xdef...,0xghi...` *(dipisahkan koma tanpa spasi)*

---

### 4️⃣ Install Dependency

```
pip install -r requirements.txt
````

---

### 5️⃣ Jalankan Bot

```
python bot.py
```

Lalu masukkan input sesuai kebutuhan:

```
Jumlah transaksi per wallet: 2
Jumlah swap per wallet: 1
Jumlah LP per wallet: 1
```

Bot akan mulai otomatis bekerja.

---

## 🧾 Struktur Project

```
├── bot.py              # File utama bot
├── checkpoint.py       # Fungsi check-in
├── config.py           # Konfigurasi token dan contract
├── requirements.txt    # Daftar library Python
├── .gitignore          # File yang tidak akan diupload ke GitHub
└── README.md           # Panduan penggunaan
```

---

## 🚫 Jangan Upload File Ini

Pastikan file `.gitignore` berisi:

```
.env
privateKeys.txt
```

> Jangan pernah menyimpan private key langsung di dalam file Python.

---

## 🔐 Keamanan

* Private key dibaca dari `.env` atau Secret Gitpod
* Tidak pernah disimpan dalam file yang diunggah
* Tidak tampil di console/log publik

---

## 📞 Kontak

Hubungi saya di Telegram:[@zibrx](https://t.me/zibrx)

---

## ✅ Selesai

Nikmati farming dan testnet otomatis di Pharos Network buatan YansDkk! 🚀
