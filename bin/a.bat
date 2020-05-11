@echo off
echo Launching virtual environment
echo Calling .\bin\Scripts\activate
echo.
echo before activation
echo environment variable for VIRTUAL_ENV=%VIRTUAL_ENV%
echo.
call .\bin\Scripts\activate
echo.
echo after activation
echo environment variable for VIRTUAL_ENV=%VIRTUAL_ENV%