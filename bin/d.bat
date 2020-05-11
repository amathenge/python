@echo off
echo Deactivating virtual environment
echo.
echo before deactivation
echo environment variable for VIRTUAL_ENV=%VIRTUAL_ENV%
echo.
call deactivate
echo.
echo after deactivation
echo environment variable for VIRTUAL_ENV=%VIRTUAL_ENV%