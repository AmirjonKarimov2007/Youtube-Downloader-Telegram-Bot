from aiogram import types
from loader import dp, bot
from data.config import ADMINS
import os
from utils.test import downloader_youtube
from aiogram.dispatcher.filters import Text
@dp.message_handler()
async def youtube_sender(message: types.Message):
    url = message.text
    id = str(message.from_user.id)
    print('yuklaniyapdi')
    youtube_video = await downloader_youtube(url, message.from_user.id)
    print('yuklandi')
    video_file_path = f'/home/amirjon/Telegram_Channels_Bot/Template-for-telegram-bot/{id}.mp4'

    # Check if the file exists before sending
    if os.path.exists(video_file_path):
        with open(video_file_path, 'rb') as video_file:
            try:
                await bot.send_video(ADMINS[-1], video_file, caption="Here is your video!")
            finally:
                os.system(f'rm -rf /home/amirjon/Telegram_Channels_Bot/Template-for-telegram-bot/{id}.mp4')