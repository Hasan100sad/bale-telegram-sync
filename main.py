import os
import requests
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# توکن‌ها از Environment Variables
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
BALE_TOKEN = os.environ.get("BALE_TOKEN")
BALE_CHAT_ID = os.environ.get("BALE_CHAT_ID")

BALE_API_URL = "https://tapi.bale.ai/bot{}/sendMessage"


async def forward_to_bale(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        text = update.message.text

        requests.post(
            BALE_API_URL.format(BALE_TOKEN),
            json={
                "chat_id": BALE_CHAT_ID,
                "text": text
            }
        )


async def main():
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_bale)
    )
    await application.run_polling()


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
