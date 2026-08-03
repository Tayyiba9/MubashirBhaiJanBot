from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8879657667:AAH5wttxLEZ2OugWdmwgG31NUHkbE8GEv8Y"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    await update.message.reply_text("Video mil gayi ✅ Upload ke liye tayyar kar raha hoon...")

app.add_handler(MessageHandler(filters.VIDEO, video_handler))
