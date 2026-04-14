# 📩 Telegram Email Sender Bot

Bot Telegram untuk mengirim email otomatis (misalnya ke support WhatsApp) berdasarkan daftar nomor HP yang dikirim oleh admin.

---

## 🚀 Fitur

- Kirim email otomatis dari Telegram
- Support multiple nomor (per baris)
- Delay antar pengiriman (anti spam)
- Bisa dihentikan dengan command `/stop`
- Hanya admin yang bisa menggunakan bot

---

## 📦 Requirements

- Python 3.8+ (disarankan 3.10+)
- Package:
  - python-telegram-bot
  - python-dotenv

---

## 📥 Install Dependencies

### Cara cepat:
pip install python-telegram-bot==20.7 python-dotenv==1.0.1

### Atau pakai requirements.txt:

Buat file `requirements.txt`:
python-telegram-bot==20.7
python-dotenv==1.0.1

Lalu install:
pip install -r requirements.txt

---

## ⚙️ Setup Environment

Buat file `.env` di folder project:

BOT_TOKEN=token_bot_kamu
EMAIL=email@gmail.com
APP_PASSWORD=password_aplikasi_gmail
TARGET_EMAIL=android@support.whatsapp.com
ADMIN_CHAT_ID=123456789

---

## 🔐 Catatan Gmail

Gunakan App Password, bukan password biasa.

Langkah:
1. Aktifkan 2FA di Gmail
2. Generate App Password
3. Pakai di APP_PASSWORD

---

## ▶️ Cara Menjalankan Bot

python bot.py

Jika berhasil:
✅ Bot jalan...

---

## 📲 Cara Pakai

### 1. Start bot
/start

### 2. Kirim nomor HP
Format:
628123456789
628987654321

Atau:
08123456789
08987654321

Bot akan:
- Kirim email satu per satu
- Delay 2 menit tiap nomor

---

### 3. Stop proses
/stop

---

## ⚠️ Penting

- Bot hanya bisa digunakan oleh ADMIN_CHAT_ID
- Jangan spam berlebihan (Gmail bisa kena limit)
- Delay default: 120 detik

---

## 🧠 Tips

Ubah delay di bagian:
await asyncio.sleep(120)

---

## 📁 Struktur Project

project/
│
├── bot.py
├── .env
└── requirements.txt

---

## ✅ Status

✔ Compatible dengan:
- python-telegram-bot v20+
- Python 3.8+

---
