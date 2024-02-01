import yt_dlp

import os
import shutil

ydl_opts = {'format': 'bestaudio/best'}
URLS = ['https://www.youtube.com/watch?v=6Nyy17k_9ds&ab_channel=Pixelbitie']
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(URLS)
    
# Исходное название файла
orig_filename = './LOBOTOMY DASH： Theme Song [6Nyy17k_9ds].webm'
# Название которое мы хотим
new_filename = './Dash.wav'
#Переименовываем файл из orig_filename в new_filename
os.rename(orig_filename, new_filename)
print(f'[rename] Os: File renamed to {new_filename}')

# Переносим файл

# Исходный путь файла
# source = './Dash.webm'
source = new_filename
# Путь, куда мы хотим переместить файл
destination = str(input('Введите путь\n>>>'))
# Перемещение файла
shutil.move(source, destination)
print(f'[move] Shutil: File moved to {destination}')