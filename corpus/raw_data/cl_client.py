import os
import socket
import codecs
from time import sleep
from urllib.error import URLError
from xml.dom.minidom import parseString
from urllib.request import Request, urlopen


# file paths
INPUT_SONGLIST_DIR = "./"
OUTPUT_RAW_DIR = "./"
if not os.name == 'posix':
    INPUT_SONGLIST_DIR = ".\\"
    OUTPUT_RAW_DIR = ".\\"

# name of songlist file
SONGLIST = "songlist.txt"

# chart lyrics api really doesn't allow more frequent requests.... timeout in s
API_TIMEOUT = 20


# Chartlyrics HTTP API
#
# http://api.chartlyrics.com/apiv1.asmx/SearchLyric?artist=string&song=string
# http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist=string&song=string
# http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=string
# http://api.chartlyrics.com/apiv1.asmx/GetLyric?lyricId=string&lyricCheckSum=string
#

# ...replace artist=string and song=string with artist=%s and song=%s for better use later on

#SEARCH_LYRIC = "http://api.chartlyrics.com/apiv1.asmx/SearchLyric?artist=%s&song=%s"
SEARCH_DIRECT = "http://api.chartlyrics.com/apiv1.asmx/SearchLyricDirect?artist=%s&song=%s"
#SEARCH_TEXT =  "http://api.chartlyrics.com/apiv1.asmx/SearchLyricText?lyricText=%s"
#GET_LYRIC = "http://api.chartlyrics.com/apiv1.asmx/GetLyric?lyricId=%s&lyricCheckSum=%s"


# load songlist from textfile, returns dict of artists:[songs, ... , ... ]
def load_songlist(file):

    # load file
    songlist =  codecs.open(file , 'r', encoding='utf-8')
    # store as list
    songlist = songlist.readlines()
    # init empty dict
    song_dict = {}

    for song in songlist:

        # if there was a empty line in the file continue...
        if song is "\n":
            continue

        # split the line in artist and song text, clean entries
        next_song = song.split(" - ",1)
        artist = next_song[0]
        song = next_song[1].replace("\n","")

        # if there is a key for the artist in the dict append the song name
        if artist in song_dict:
            song_dict[artist].append(song)
        # if there is no key yet, create a new list with the song as first entry
        else:
            song_dict[artist] = [song]

        print("Load: " + artist + " - " + song)
        #print(song_dict)

    return song_dict


# perform api call given artist and song, returns TRUE and FALSE on success/fail.
def getLyric(artist, song):

    # build the api call with template and variables. NOTE: Replace space " " with "+" for songs as it's the end of string and would lead otherwise to invalid API calls!!!
    api_call = SEARCH_DIRECT % (artist, song.replace(" ", "+"))
    print("Download: " + artist +" - " + song + " API-CALL: " + api_call)
    request = Request(api_call)

    # perform API call
    try:
        response = urlopen(request, timeout=5)
        #print(response.headers['content-type'])

    # catch ERRORS, print them and return false
    except URLError as e:
        print("Error: ", e)
        return False
    except socket.error as e:
        print("Error: ", e)
        return False

    # In case of success, parse the response to XML
    lyric_xml_dom = parseString(response.read())
    # Close the socket
    response.close()
    #print lyric_dom

    # Parse XML dom for, ARTIST, SONGNAME and the LYRICS. CLEAN some characters which can lead to problems when saving.
    la = lyric_xml_dom.getElementsByTagName("LyricArtist")[0].firstChild.nodeValue
    la = la.replace(u'/','')

    ls =  lyric_xml_dom.getElementsByTagName("LyricSong")[0].firstChild.nodeValue
    ls = ls.replace(u'.','')

    l = lyric_xml_dom.getElementsByTagName("Lyric")[0].firstChild.nodeValue
    #print(type(l))

    # compose a new filename, open it, write lyric to it
    new_song_file = la+"_"+ls+".txt"
    target = codecs.open(OUTPUT_RAW_DIR + new_song_file , 'w', encoding='utf-8')
    target.write(l)
    target.close()

    print("Success! Saved file: " + OUTPUT_RAW_DIR + new_song_file)
    return True


'''
HERE STARTS THE ACTUAL SCRIPT

'''

# Load data from file
print("Load Data from: " + INPUT_SONGLIST_DIR+SONGLIST)
song_list = load_songlist(INPUT_SONGLIST_DIR+SONGLIST)

# Loop over all entries in the song dict and download Lyrics
for artist in song_list:
    for song in song_list[artist]:

        while not getLyric(artist, song):
            print("\nwait for %s seconds...\n" % (API_TIMEOUT))
            sleep(API_TIMEOUT)
        else:
            print("\nwait for %s seconds...\n" % (API_TIMEOUT))
            sleep(API_TIMEOUT)


print(" Finished ")
