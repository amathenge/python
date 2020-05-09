@echo off
rem
rem create a virtual environment
rem
rem run from the folder from which you want to create the environment.
rem
rem for example, if your folder structure is:
rem
rem c:\users\andrew\documents\src\python
rem
rem and you want to create an application in:
rem
rem c:\users\andrew\documents\src\python\myapp
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
rem 11.  makes the following folders:
rem	        application
rem	        application\templates
rem	        application\templates\includes
rem	        application\static
rem	        application\static\css
rem	        application\static\images
rem 12.	 copies the file "main.py" from "..\bin\templates" into "."
rem 13.  copies the file "routes.py" from "..\bin\templates" into "application"
rem 14.  copies the file "__init__.py" from "..\bin\templates" into "application"
rem 15.  copies the file "index.html" from "..\bin\templates" into "application\templates"
rem 16.  exits with the following help message:
rem         to activate virtual environment, from "." type "a"
rem         to deactivate virutal environment from "." type "d"
rem         to start a flask shell type "flask shell"
rem         to start the flask application type "flask run"
rem
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
echo Step 11 - Creating template folders and copying files
echo.
echo mkdir application
mkdir application
echo makedir templates
mkdir templates
echo mkdir templates\includes
mkdir templates\includes
echo mkdir static
mkdir static
echo mkdir static\css
mkdir static\css
echo mkdir static\scripts
mkdir static\scripts
echo.
echo Step 12, 13, 14 and 15 copy files to folder locations
echo.
echo copy ..\bin\templates\index.html templates
copy ..\bin\templates\index.html templates
echo copy ..\bin\templates\main.py .
copy ..\bin\templates\main.py .
echo copy ..\bin\templates\routes.py application
copy ..\bin\templates\routes.py application
echo copy ..\bin\templates\__init__.py application
copy ..\bin\templates\__init__.py application
echo.
echo Step 15:
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
echo call d.bat
call d.bat
goto completed

:ExitScript
echo Usage .\bin\mkenv.bat
echo Project folder cannot be blank
goto completed

:ExistFolder
echo Folder %proj% exists. Please choose a different folder
goto completed

:UserQuit
echo "Exiting..."
goto completed

:completed
echo.
echo.