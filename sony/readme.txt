In Archive
---------------------------------------------------------------------
NOTE
 +---------------------------------------------------+
 | Run the file README.BAT for a quick summary |
 +---------------------------------------------------+

1. Create a virtual environment and get taglib (pip install pytaglib)

2. +----------------+
   | Run genlist.py |
   +----------------+
   A file called sonysongs.txt will be created.
   
3. +----------------+
   | Run toexcel.py | = create a file (songs.txt) with the following columns
   +----------------+
   song_length | song_path | song_artist_title
   
4. +------------------+
   | Import songs.txt | into a new sheet in the xlsx file
   +------------------+
   Example: sheet = Sony4

5. Add the required columns at the end for the M3U data (E, F, G, H, I and J)
                            +-------------------------+
6. Run the compare function | "Sub CompareImported()" |
                            +-------------------------+
   In this function, change the sheets to compare TO/FROM
   Example:
     fromSheet = "Sony3"
     toSheet = "Sony4"
   This should result in 1's put in the appropriate columns in Sony4
   
7. Update the columns (in Sony4) to add the songs to the playlist
                    +-----------------------+
8. Run the function | "Sub WriteSelected()" | - this is a Workbook function.
                    +-----------------------+
   NB: you may encounter another one - that was a testing one.

9. Run it to produce the required files:
   TonySoft.m3u, TonySoul.m3u, TonyReggea.m3u, and so on.
   
10.+-----------------+
   | Run process.bat |
   +-----------------+
   This will created the shuffled versions of the files:
   TonySoft_Shuffled.m3u, TonySoul_Shuffled.m3u, TonyReggea_Shuffled.m3u, and so on.
   
11. Run cleanup.bat = THIS IS CALLED AUTOMATICALLY AFTER PROCESS.BAT
   This will delete the unshuffled files, and rename the shuffled ones.

12. Copy to device - making sure you delete the existing ones.
        +--------------------+
13. Run | cleanup_folder.bat |
        +--------------------+


----------------- STUFF BELOW IS ALL OLD --------------------------

mkm3u.py
  will generate a playlist from all the files in the sony mp3 player.
  
  python mkm3u.py --walk playlist.m3u d:\MUSIC
  (the case on the foldername is important))
  
shuf.py
  will shuffle the files in playlist.m3u (read the file for the actual name)
  and create a new playlist "softlist.m3u" (hardcoded).
  
