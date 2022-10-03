from telethon import *
import telebot
import librosa
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import librosa.display

api_id = 16951751
api_hash = '7b5431b2d578c98daa45a8c82d97b558'
client = TelegramClient('anon', api_id, api_hash)
bot_token = '5502801392:AAHb34mCIfa0F-HguUoa0V6YDAandmSIxlQ'
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage())
async def main(event):
    if event.audio:
        async with bot:
            audio = await client.download_media(event.audio)
            y, sr = librosa.load(audio)
            tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
            result = str(int(float(tempo)))
            await event.reply(result)


client.start()
client.run_until_disconnected()
