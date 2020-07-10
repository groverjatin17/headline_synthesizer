REM @echo off
REM call venv\Scripts\activate.bat
REM python scripts\main.py
REM pause
@ECHO off
cls
:start
ECHO.
ECHO 1. Scrap and Read headlines from WION
ECHO 2. Scrap and Read headlines from InShorts
set choice=
set /p choice=Type the number to print text.
if not '%choice%'=='' set choice=%choice:~0,1%
if '%choice%'=='1' goto Wion
if '%choice%'=='2' goto Inshorts
ECHO "%choice%" is not valid, try again
ECHO.
goto start
:Wion
call venv\Scripts\activate.bat
python scripts\main.py --newsChannel wion
goto end
:Inshorts
call venv\Scripts\activate.bat
python scripts\main.py --newsChannel inshorts
goto end
:end
pause