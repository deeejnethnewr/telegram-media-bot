from pyrogram import Client, filters
from pytube import Playlist
import os
from keep_alive import keep_alive

API_ID = 12345678
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client("my_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

keep_alive()  # Keep Replit running

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("🎥 YouTube Playlist Downloader Bot is Online!")

@app.on_message(filters.text & filters.private)
async def download_playlist(client, message):
    url = message.text
    if "playlist" in url:
        playlist = Playlist(url)
        for video in playlist.videos:
            filename = video.streams.get_highest_resolution().download()
            await message.reply_video(video=filename)
            os.remove(filename)

app.run()
