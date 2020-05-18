@echo off
rem

rem - create a virtual environment for flask training
rem - without the development files.

rem
rem run this from "c:\users\andrew\documents\src\python"
rem
rem usage:
rem
rem     .\bin\mkenv.bat <envname>
rem
rem what it does:
rem
rem 1.   asks for project folder name <proj> and creates the folder
rem 2.   changes into <proj> folder
rem 3.   copies "a.bat" and "d.bat" into <proj>
rem 4.   runs "python -m venv bin"  - bin is where the Python virtual environment scripts will be kept
rem 5.   activating the shell
rem 6.   runs "python -m pip install --upgrade pip"
rem 7.   runs "pip install flask"
rem 8.   runs "pip install flask-wtf"
rem 9.   runs "pip install python-dotenv"
rem 10.  copies the file ".flaskenv" from "..\bin\templates"
rem         to start the flask application type "flask run"
rem
call C:\Users\andrew\Documents\src\python\bin\envcheck.py %~0
if not "%errorlevel%" == "0" goto checkFolder
set proj=
set /p proj="Enter Project Folder Name: "
if "%proj%" == "" goto ExitScript
if exist %proj% goto ExistFolder
echo Step 1.0 - creating the project folder
mkdir %proj%
echo.
echo Step 1.1 - changing into project folder
cd .\%proj%
dir
echo.
echo Step 3 - copying batch files to automate activating and deactivating virtual environment
echo.
echo copy ..\bin\a.bat .
copy ..\bin\a.bat .
echo copy ..\bin\d.bat .
copy ..\bin\d.bat .
dir
echo.
echo Step 4 - creating virtual environment
echo.
echo python -m venv bin
python -m venv bin
echo.
echo dir
dir
echo.
echo Step 5 - activating the virtual environment
echo call a.bat
call a.bat
echo.
echo %PROMPT%
if NOT "%PROMPT%" == "(bin) $P$G" goto UserQuit
echo.
echo Python Packages
echo Step 6 - upgrading pip
echo.
echo python -m pip install --upgrade pip
python -m pip install --upgrade pip
echo.
echo Step 7 - installing flask
echo.
echo pip install flask
pip install flask
echo.
echo Step 8 - installing flask-wtf
echo.
echo pip install flask-wtf
pip install flask-wtf
echo.
echo Step 9 - installing python-dotenv
echo.
echo pip install python-dotenv
pip install python-dotenv
echo.
echo Step 10 - Copying Flask environment file
echo copy ..\bin\temlates\.flaskenv .
copy ..\bin\templates\.flaskenv .
echo.
echo Step 11:
echo to activate virtual environment, from "." type "a"
echo then check to see that the flask app, and dependencies were installed
echo by typing "pip list"
echo.
echo.
echo pip list
pip list
echo.
echo.
echo we're done!
echo.
echo call d.bat to exit from the virtual environment
call d.bat
echo.
echo.
echo Helpfull notes:
echo ---------------
echo.
echo These commands work in the root folder (where main.py is located)
echo.
echo To launch the virtual environment, type "a"
echo To close the virtual environment, type "d"
echo To launch a python shell - with flask - type "flask shell"
echo To launch your application, flask server, type "flask run"  ^<--this is what you want do to
echo.
echo To move the application to a different location, simply copy the entire folder
echo %proj%
echo To the new location.
goto completed

:ExitScript
echo Usage .\bin\mkenv.bat
echo Project folder cannot be blank
goto completed

:ExistFolder
echo Folder %proj% exists. Please choose a different folder
goto completed

:UserQuit
echo "Exiting... after running a.bat to set environment"
goto completed

:checkFolder
echo Appears that we are running from a strange location. The script should
echo be run from C:\Users\Andrew\Documents\src\python
echo.
call C:\Users\andrew\Documents\src\python\bin\envcheck.py %~0
echo check completed with errorlevel = %errorlevel%
echo.
echo Please check
goto completed


:completed
echo.
echo.