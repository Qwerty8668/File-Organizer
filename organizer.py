import os
from pathlib import Path
import shutil

audio = (".mp3", ".wav")

img = (".img", ".jpg", ".gif", ".png", ".svg")

pdf = (".pdf")

calc = (".xlsx", ".csv")

text = (".doc", ".docx", ".txt", ".odt")

video = (".mp4")


def is_audio(ext):
    return ext in audio

def is_img(ext):
    return ext in img

def is_pdf(ext):
    return ext in pdf

def is_calc(ext):
    return ext in calc

def is_text(ext):
    return ext in text

def is_video(ext):
    return ext in video

print(os.getcwd())

directory = input("Input directory (e.g. C:/Users/DOMOWY_PC/Desktop/test/): ")

os.chdir(directory)

#print(os.listdir())

Path("audio").mkdir(exist_ok = True)
Path("img").mkdir(exist_ok = True)
Path("pdf").mkdir(exist_ok = True)
Path("excel").mkdir(exist_ok = True)
Path("text").mkdir(exist_ok = True)
Path("video").mkdir(exist_ok = True)


filesList = os.listdir()

for file in filesList:
    
    print(file)

    name, extention = os.path.splitext(file)

    print(extention)

    if extention == '':
        continue
    
    if is_audio(extention):
        shutil.move(file, directory + "audio")    
    elif is_img(extention):
        shutil.move(file, directory + "img")
    elif is_pdf(extention):
        shutil.move(file, directory + "pdf")
    elif is_calc(extention):
        shutil.move(file, directory + "excel")
    elif is_text(extention):
        shutil.move(file, directory + "text")
    elif is_video(extention):
        shutil.move(file, directory + "video")
    