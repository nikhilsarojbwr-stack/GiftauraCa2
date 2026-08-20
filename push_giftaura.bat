@echo off
title GiftAura+ - GitHub Push

cd /d D:\Gift

echo.
echo ==========================================
echo        GiftAura+ GitHub Auto Update
echo ==========================================
echo.

REM ==========================================
REM CHECK GIT
REM ==========================================

echo Checking Git installation...

if not exist "C:\Program Files\Git\cmd\git.exe" (
    echo.
    echo ERROR: Git was not found at:
    echo C:\Program Files\Git\cmd\git.exe
    echo.
    pause
    exit /b 1
)

echo Git found.
echo.

REM ==========================================
REM CHECK REPOSITORY
REM ==========================================

if not exist ".git" (
    echo ERROR: D:\Gift is not a Git repository.
    echo.
    echo Run these commands once:
    echo.
    echo git init
    echo git remote add origin https://github.com/nikhilsarojbwr-stack/GiftauraCa2.git
    echo git branch -M main
    echo.
    pause
    exit /b 1
)

REM ==========================================
REM ADD CHANGES
REM ==========================================

echo [1/3] Adding changes...
echo.

"C:\Program Files\Git\cmd\git.exe" add .

if errorlevel 1 (
    echo.
    echo ERROR: Failed to add files.
    echo.
    pause
    exit /b 1
)

echo.
echo Files added successfully.
echo.

REM ==========================================
REM COMMIT
REM ==========================================

echo [2/3] Creating commit...
echo.

set "commit_message="
set /p "commit_message=Enter commit message: "

if "%commit_message%"=="" (
    set "commit_message=GiftAura+ update"
)

"C:\Program Files\Git\cmd\git.exe" commit -m "%commit_message%"

echo.

REM ==========================================
REM PUSH
REM ==========================================

echo [3/3] Pushing to GitHub...
echo.

"C:\Program Files\Git\cmd\git.exe" push origin main

if errorlevel 1 (
    echo.
    echo ==========================================
    echo             PUSH FAILED
    echo ==========================================
    echo.
    echo Check the error message above.
    echo.
    pause
    exit /b 1
)

REM ==========================================
REM SUCCESS
REM ==========================================

echo.
echo ==========================================
echo       GitHub Update Successful!
echo ==========================================
echo.
echo Your GiftAura+ project has been pushed.
echo.
echo Repository:
echo https://github.com/nikhilsarojbwr-stack/GiftauraCa2
echo.

pause