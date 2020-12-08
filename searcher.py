from youtubesearchpython import SearchPlaylists
from youtubesearchpython import SearchVideos
import downloader
import os

def playlists_search():
    print('')
    print('------- YOUTUBE SEARCH ENGINE PLAYLISTS --------')
    print('')
    search_term = input('Search playlist: ')

    search = SearchPlaylists(search_term, max_results=5, mode='dict')

    for v in search.result()['search_result']:
        print('------------------------------------------------')
        print('')
        print('index: ' + str(v['index']))
        print('title: ' + v['title'])
        print('count: ' + v['count'])
        print('channel: ' + v['channel'])
        print('link: ' + v['link'])
        print('')
        print('------------------------------------------------')

def songs_search():
    print('')
    print('--------- YOUTUBE SEARCH ENGINE SONGS ----------')
    print('')
    search_term = input("Search song / video: ")
    search = SearchVideos(search_term, max_results=5, mode='dict')
    for v in search.result()['search_result']:
        print('------------------------------------------------')
        print('')
        print('index: ' + str(v['index']))
        print('title: ' + v['title'])
        print('channel: ' + v['channel'])
        print('views: ' + str(v['views']))
        print('link: ' + v['link'])
        print('')
        print('------------------------------------------------')

    print('')
    print('------------------------------------------------')
    print('What do you want to do next?')
    print('(1) Download the song')
    print('(2) Add the song to a playlist')
    answer = input('choice: ')
    print('------------------------------------------------')
    print('')

    if answer == '1':
        index = input('index of the song: ')
        url = search.result()['search_result'][int(index)]['link']
        name = input('name of the song: ')

        downloader.song_download_var(url, name)

    elif answer == '2':
        index = input('index of the song: ')

        url = search.result()['search_result'][int(index)]['link']
        name = input('name of the song: ')
        print('')
        print('------------------ PLAYLISTS -------------------')
        print('')

        folder = os.listdir("/Users/alexander/Documents/music/playlists/")
        num = 0
        for i in folder:
            print('------------------------------------------------')
            print('')
            print('index: ' + str(num))
            print('name: ' + str(i))
            print('')
            print('------------------------------------------------')
            num += 1
        print('')
        folder_playlist = input('playlist index for the song: ')

        playlist = folder[int(folder_playlist)]

        downloader.song_download_playlist(url, name, playlist)