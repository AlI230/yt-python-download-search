from pytube import YouTube, Playlist
import os
import moviepy.editor as mp
import re

def playlist_download():
    print('')
    print('---------- YOUTUBE PLAYLIST DOWNLOAD -----------')
    print('')
    url = input("Link to playlist: ")
    name = input("Name of playlist: ")
    print('')

    playlist = Playlist(url)

    for url in playlist:
        print('------------------------------------------------')
        print('')
        print(((YouTube(url)).title))
        print('')
        print('------------------------------------------------')
        print('')
        print("Downloading....")
        YouTube(url).streams.get_lowest_resolution().download(output_path="/Users/alexander/Documents/music/playlists/" + name + "/")
        print("Downloaded!")

    folder = "/Users/alexander/Documents/music/playlists/" + name + "/"
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    print('\n Complete \n')

def song_download():
    print('')
    print('------------ YOUTUBE SONG DOWNLOAD -------------')
    print('')
    url = input("Link to song: ")
    name = input("Name of song: ")
    print('')
    print('------------------------------------------------')
    print('')
    print(((YouTube(url)).title))
    print('')
    print('------------------------------------------------')
    print('')

    print("Downloading....")
    YouTube(url).streams.get_audio_only().download(filename=name, output_path="/Users/alexander/Documents/music/songs/" )
    print("Downloaded!")

    folder = "/Users/alexander/Documents/music/songs"
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    # Completion
    print("\n Complete \n")

def song_download_var(url, name):
    print('')
    print('------------ YOUTUBE SONG DOWNLOAD -------------')
    print('------------------------------------------------')
    print('')
    print(((YouTube(url)).title))
    print('')
    print('------------------------------------------------')
    print('')

    print("Downloading....")
    YouTube(url).streams.get_audio_only().download(filename=name, output_path="/Users/alexander/Documents/music/songs/" )
    print("Downloaded!")

    folder = "/Users/alexander/Documents/music/songs"
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    # Completion
    print("\n Complete \n")

def song_download_playlist(url, name, playlist):
    print('')
    print('------------ YOUTUBE SONG DOWNLOAD -------------')
    print('------------------------------------------------')
    print('')
    print(((YouTube(url)).title))
    print('')
    print('------------------------------------------------')
    print('')

    print("Downloading....")
    YouTube(url).streams.get_audio_only().download(filename=name, output_path="/Users/alexander/Documents/music/playlists/" + playlist + "/")
    print("Downloaded!")

    folder = "/Users/alexander/Documents/music/songs"
    for file in os.listdir(folder):
        if re.search('mp4', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)

    # Completion
    print("\n Complete \n")

def video_download():
    print('')
    print('------------ YOUTUBE VIDEO DOWNLOAD ------------')
    print('')
    url = input("Link to video: ")
    name = input("Name of video: ")
    print('')
    print('------------------------------------------------')
    print('')
    print(((YouTube(url)).title))
    print('')
    print('------------------------------------------------')
    print('')

    # Downloading
    print("Downloading....")
    YouTube(url).streams.get_highest_resolution().download(filename=name, output_path="/Users/alexander/Documents/music/videos/")
    print("Downloaded!") 

    print('\n Complete \n')