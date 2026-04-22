import os
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filter

TOKEN = os.getenv("TOKEN")

AUDIO_FILE = "meditation.mp3"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    if "тишина" in text:

        await update.message.reply_text(
            "Ты вошёл в пространство тишины.\n\n"
            "Сделай вдох...\nи медленный выдох.\n\n"
            "Просто побудь здесь."
        )

        await asyncio.sleep(3)

        await update.message.reply_audio(
            audio=open(AUDIO_FILE, "rb"),
            caption="Закрой глаза и слушай."
        )

        await asyncio.sleep(5)

        keyboard = [
            [InlineKeyboardButton("Идти глубже", url="https://t.me/your_channel")]
        ]

        await update.message.reply_text(
            "Хочешь продолжить?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    else:
        await update.message.reply_text(
            "Напиши слово «тишина»"
        )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")
app.run_polling()
