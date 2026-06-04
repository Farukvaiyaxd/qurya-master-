import os
from pyrogram import Client, enums
from dotenv import load_dotenv

# config.env ফাইল লোড করা
load_dotenv("config.env")

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client(
    "master_bot",
    api_id=int(API_ID),
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="tools"), # tools ফোল্ডারের ফাইলগুলো অটোমেটিক লোড হবে
    parse_mode=enums.ParseMode.HTML
)

if __name__ == "__main__":
    print("🚀 Bot is starting Raining on...")
    app.run()
