from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "YAHAN_APNA_TELEGRAM_BOT_TOKEN_LIKHEN"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot chal raha hai ✅")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
