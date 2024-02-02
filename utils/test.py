from pytube import YouTube
from yt_dlp import YoutubeDL

async def downloader_youtube(url, user_id):
    try:
        link = url
        user_id_str = str(user_id)
        video = YouTube(link)
        video_stream = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

        if video_stream:
            video_stream.download(filename=f'{user_id_str}.mp4')
            print(f'Download complete for user {user_id_str}')
            return video_stream
        else:
            print(f'No progressive stream available for the given video. User: {user_id_str}')
            return None
    except:
        link = url
        ydl_opts = {
        'outtmpl': f'/home/amirjon/Telegram_Channels_Bot/Template-for-telegram-bot/{user_id}.mp4',
        'age_limit': 18,
    }

        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            return ydl.prepare_filename(info_dict)
        return None
