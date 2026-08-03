from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8879657667:AAH5wttxLEZ2OugWdmwgG31NUHkbE8GEv8Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
