import os
import sys
import getopt
# import mad
# import ID3
from mutagen.id3 import ID3
from mutagen.mp3 import MP3

__doc__ = "Generate m3u playlists (default: local dir)"
__author__ = "Andrew Mathenge <andrew@mathenge.ca>"
__date__ = "16 June, 2020"
__version__ = "1.0"

"""
A simple m3u file is like this:

#EXTM3U
#EXTINF:111,Coldplay - In Myplace
/path/to/the/song/Coldplay - In My Place.mp3

- #EXTM3U is the format descriptor (unchanging)
- #EXTINF is the record marker (with extended info, unchanging)
- : is the separator
- 111 is the length of the track in whole seconds
- , is the other separator
- the name of the track (a good generator parses the ID3,
  if there isn't an ID3 use the file name without the extension)
- /path/etc. etc. is the absolute (or relative) path to the file name
  of the track

Requirements:

- Python 3.x
- mutagen for the mp3 and id3 functions
  MP3() get the length of the track.
  ID3() get the artist and title from the mp3 tags in the file.

Notes:
- Some of the options are not in use (e.g., --walk) - a file with the list is required
  The filename is songlist.txt

"""

FORMAT_DESCRIPTOR = "#EXTM3U"
RECORD_MARKER = "#EXTINF"


def _usage():
    """ print the usage message """
    msg = "Usage:  pyM3U.py [options] playlist_name [path]\n"
    msg += __doc__ + "\n"
    msg += "Options:\n"
    msg += "%5s,\t%s\t\t%s\n" % ("-n", "--no-sort", "do not sort entries by filename")
    msg += "%5s,\t%s\t\t\t%s\n" % ("-w", "--walk", "walk into subdirs (default: no walk)")
    msg += "\n%5s,\t%s\t\t\t%s\n\n" % ("-h", "--help", "display this help and exit")

    print(msg)

def generate_list(name="songs_list.m3u", path=".",
                  sort=True, walk=False):
    """ generates the M3U playlist with the given file name

    and in the given path """

    fp = None
    songFile = None
    try:
        try:
            """
            if walk:
                # recursive version
                mp3_list = [os.path.join(root, i) for root, dirs, files in os.walk(path) for i in files \
                            if i[-3:] == "mp3"]
            else:
                # non recursive version
                mp3_list = [i for i in os.listdir(path) if i[-3:] == "mp3"]

            """
            
            #print mp3_list

            songFile = open('songlist.txt','r')
            mp3_list = songFile.read().split('\n')

            if sort:
                mp3_list.sort()

            fp = open(name, "w")
            fp.write(FORMAT_DESCRIPTOR + "\n")

            for track in mp3_list:
                if not walk:
                    track = os.path.join(path, track)
                else:
                    track = os.path.abspath(track)
                # open the track with mad and ID3
                # mf = mad.MadFile(track)
                mf = MP3(track)
                # id3info = ID3.ID3(track)
                try:
                    id3info = ID3(track)
                except:
                    id3info = None
                    
                # M3U format needs seconds but
                # total_time returns milliseconds
                # hence i convert them in seconds
                # track_length = mf.total_time() / 1000
                track_length = int(mf.info.length)
        
                # get the artist name and the title
                # artist, title = id3info.artist, id3info.title
                try:
                    artist, title = id3info['TPE1'].text[0], id3info['TIT2'].text[0]
                except:
                    artist = ''
                    title = ''

                # if artist and title are there
                try:
                    if artist and title:
                        fp.write(RECORD_MARKER + ":" + str(track_length) + "," +\
                                 artist + " - " + title + "\n")
                    else:
                        fp.write(RECORD_MARKER + ":" + str(track_length) + "," +\
                                 os.path.basename(track)[:-4] + "\n")
                except:
                    fp.write('AN ERROR OCCURED WITH THIS RECORD HEADER\n')
                    
                # write the fullpath
                modified_track = track[9:]
                try:
                    fp.write(modified_track + "\n")
                except:
                    fp.write('AN ERROR OCCURED WRITING THE FILENAME\n')
                
        except (OSError, IOError) as e:
            print(e)
    finally:
        if fp:
            fp.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stderr.write("No playlist name given\n")
        sys.exit(1)
        
    options = "nhw"
    long_options = ["no-sort", "help", "walk"]

    try:
        opts, args = getopt.getopt(sys.argv[1:], options, long_options)
    except getopt.GetoptError:
        print("error")
        _usage()
        sys.exit(2)

    name, path, sort = "songs_list.m3u", ".", True
    walk = False

    #print opts, args

    # check cmd line args
    for o, a in opts:
        if o in ("-n", "--no-sort"):
            sort = False
        if o in ("-w", "--walk"):
            walk = True
        if o in ("-h", "--help"):
            _usage()
            sys.exit(1)

    try:
        name = args[0]
    except:
        pass
            
    try:
        path = args[1]
    except:
        pass

    #print name, path, sort

    if os.path.exists(path):
        generate_list(name, path, sort, walk)
    else:
        sys.stderr.write("Given path does not exist\n")
        sys.exit(2)
        
        