import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Yoh! 👋 I'm your new chatbot friend. "
        "I'm still learning, but I'm happy to chat with you!"
    )



async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.lower().strip()

    if "how are you" in message:
        response = "I'm doing great! 😊 Thanks for asking. How are you?"
    elif "hello" in message or "hi" in message:
        response = "Yoh! 👋 Good to hear from you!"
    elif "your name" in message:
        response = "Bishop! ♟️ Your friendly chatbot."
    elif "thank you" in message or "thanks" in message:
        response = "You're welcome! 😄"
    else:
        response = f"You said: {message}\n\nI'm listening! 😊"

    await update.message.reply_text(response)



def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    if not token:
        raise RuntimeError("Please set the TELEGRAM_BOT_TOKEN environment variable.")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, reply)
    )

    print("Bot is running! Open Telegram and send it a message.")
    app.run_polling()


if __name__ == "__main__":
    main()
