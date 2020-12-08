#!/usr/local/bin/python3

import searcher
import downloader

while True:
    print('')
    print('------------------------------------------------')
    print('---------- YOUTUBE DOWNLOAD / SEARCH -----------')
    print('Select option you want to do: ')
    print('(1) Download Playlists, songs or videos')
    print('(2) Search Playlists, songs or videos')
    print('(quit) Quit Program')
    options = input("choice: ")
    print('------------------------------------------------')
    print('')

    if options == '1':
        print('')
        print('--------------- YOUTUBE DOWNLOAD ---------------')
        print('Select option you want to do: ')
        print('(1) Download a playlist from youtube')
        print('(2) Download a song from youtube')
        print('(3) Download a video from youtube')
        print('(quit) Quit Program')
        answer = input("choice: ")
        print('------------------------------------------------')
        print('')

        if answer == '1':
            downloader.playlist_download()

        elif answer == '2':
            downloader.song_download()
            
        elif answer == '3':
            downloader.video_download()
        
        elif answer == 'quit':
            answer = input('Are you sure you want to quit? (y/n): ')
            if answer == 'y':
                print('Program is shutting down, thank you for using!')
                break

    elif options == '2':
        print('')
        print('---------------- YOUTUBE SEARCH ----------------')
        print('Select option you want to do: ')
        print('(1) Search playlists from youtube')
        print('(2) Search a song from youtube')
        print('(quit) Quit Program')
        answer = input("choice: ")
        print('------------------------------------------------')
        print('')

        if answer == '1':
            searcher.playlists_search()

        elif answer == '2':
            searcher.songs_search()
        
        elif answer == 'quit':
            answer = input('Are you sure you want to quit? (y/n): ')
            if answer == 'y':
                print('Program is shutting down, thank you for using!')
                break

    elif options == 'quit':
        answer = input('Are you sure you want to quit? (y/n): ')
        if answer == 'y':
            print('Program is shutting down, thank you for using!')
            break
    else:
        print('No valid option')