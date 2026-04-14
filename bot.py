import smtplib
import asyncio
import os
from email.mime.text import MIMEText
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv

# Load ENV
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
TARGET_EMAIL = os.getenv("TARGET_EMAIL")  # android@support.whatsapp.com
ADMIN_CHAT_ID = int(os.getenv("ADMIN_CHAT_ID"))

running = False


# ✅ Cek admin
def is_admin(update: Update):
    return update.effective_chat.id == ADMIN_CHAT_ID


# ✅ Kirim email (format sesuai SS)
def send_email(number):
    # Pastikan format +62 / internasional
    number = f"+{number}" if not number.startswith("+") else number

    msg = MIMEText(number)
    msg["Subject"] = number
    msg["From"] = EMAIL
    msg["To"] = TARGET_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)


# ✅ /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not is_admin(update):
        return

    await update.message.reply_text(
        "Masukkan nomor HP:\n62xxxx\n(Bisa banyak, pisah per baris)"
    )


# ✅ /stop
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running

    if not is_admin(update):
        return

    running = False
    await update.message.reply_text("❌ Proses dihentikan")


# ✅ Handle input nomor
async def handle_numbers(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global running

    if not is_admin(update):
        return

    running = True
    numbers = update.message.text.splitlines()

    for i, number in enumerate(numbers, start=1):
        if not running:
            break

        msg = await update.message.reply_text(f"⏳ Proses {i}: {number}")

        try:
            send_email(number)
            await msg.edit_text(f"✅ Sukses {i}: {number}")
        except Exception as e:
            await msg.edit_text(f"❌ Gagal {i}: {number}\n{e}")

        # Delay (2 menit)
        if i != len(numbers) and running:
            info = await update.message.reply_text("⏱ Cooldown 2 menit...")
            await asyncio.sleep(120)
            await info.delete()


# ✅ Main
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_numbers))

    print("✅ Bot jalan...")
    app.run_polling()


if __name__ == "__main__":
    main()
