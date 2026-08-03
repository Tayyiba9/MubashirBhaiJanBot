import os
import pickle

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow


# Telegram Bot Token
TOKEN = "8879657667:AAH5wttxLEZ2OugWdmwgG31NUHkbE8GEv8Y"


# YouTube Permission
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload"
]


# Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot ready hai ✅\nVideo bhej kar test karein."
    )


# YouTube Upload Function
def youtube_upload(file_path):

    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:

        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)


    youtube = build(
        "youtube",
        "v3",
        credentials=creds
    )


    request = youtube.videos().insert(
        part="snippet,status",

        body={
            "snippet": {
                "title": "Telegram Upload Video",
                "description": "Uploaded using Telegram Bot"
            },

            "status": {
                "privacyStatus": "private"
            }
        },

        media_body=MediaFileUpload(
            file_path
        )
    )


    response = request.execute()

    return response



# Receive Video
async def video_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "Video receive ho gayi ✅"
    )


    video = update.message.video


    file = await context.bot.get_file(
        video.file_id
    )


    file_path = "video.mp4"


    await file.download_to_drive(
        file_path
    )


    await update.message.reply_text(
        "Video download ho gayi ✅\nYouTube upload start ho raha hai..."
    )


    try:

        youtube_upload(file_path)


        await update.message.reply_text(
            "YouTube upload complete ✅"
        )


    except Exception as e:

        await update.message.reply_text(
            f"Error: {e}"
        )



# Bot Setup
app = Application.builder().token(TOKEN).build()


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)


app.add_handler(
    MessageHandler(
        filters.VIDEO,
        video_handler
    )
)



print("Bot Running...")


app.run_polling()
