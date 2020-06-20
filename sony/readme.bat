@echo off
rem
rem print out instructions for creating a playlist.
rem
echo.
echo.
echo Mount the Sony walkman. 
echo.
echo Run  "python genlist.py"    YOU NEED A PYTHON VIRTUAL ENV WITH pytaglib
echo.
echo Run  "python toexcel.py" 
echo.
echo  Import the file songs.txt  into a new sheet in "sony.xlsm"
echo.
echo Name the sheet (e.g., Sony4)
echo.
echo Run  "Sub CompareImported()"  - this is a Workbook function
echo You will need to update a couple of variables (e.g, fromSheet, toSheet and number of rows)
echo.
echo Run  "Sub WriteSelected()"  - this is a Workbook function
echo You will need to update a couple of variables
echo.
echo Run  "process.bat" 
echo.
echo Copy the files to the Sony Walkman (all the .m3u files)
echo Delete the ones on the device. They are in D:\MUSIC
echo.
echo Run  "cleanup_folder.bat" 
echo.
echo That's ALL.