@echo off
title GiftAura+ - GitHub Auto Push

cd /d D:\Gift

echo.
echo ==========================================
echo       GiftAura+ GitHub Auto Push
echo ==========================================
echo.

REM ============================================================
REM 1. CHECK GIT
REM ============================================================

echo [1/6] Checking Git installation...
echo.

if not exist "C:\Program Files\Git\cmd\git.exe" (
    echo ERROR: Git was not found.
    echo.
    echo Expected:
    echo C:\Program Files\Git\cmd\git.exe
    echo.
    pause
    exit /b 1
)

echo Git found successfully.
echo.

REM ============================================================
REM 2. CHECK GIT REPOSITORY
REM ============================================================

echo [2/6] Checking Git repository...
echo.

if not exist ".git" (
    echo ERROR: D:\Gift is not a Git repository.
    echo.
    echo Run these commands manually once:
    echo.
    echo git init
    echo git remote add origin https://github.com/nikhilsarojbwr-stack/GiftauraCa2.git
    echo git branch -M main
    echo git push -u origin main
    echo.
    pause
    exit /b 1
)

echo Git repository found.
echo.

REM ============================================================
REM 3. CHECK REMOTE
REM ============================================================

echo [3/6] Checking GitHub remote...
echo.

"C:\Program Files\Git\cmd\git.exe" remote -v

echo.

REM ============================================================
REM 4. ADD CHANGES
REM ============================================================

echo [4/6] Adding project changes...
echo.

"C:\Program Files\Git\cmd\git.exe" add .

if errorlevel 1 (
    echo.
    echo ==========================================
    echo          ERROR: GIT ADD FAILED
    echo ==========================================
    echo.
    pause
    exit /b 1
)

echo Changes added successfully.
echo.

REM ============================================================
REM 5. COMMIT
REM ============================================================

echo [5/6] Creating commit...
echo.

set "commit_message="
set /p "commit_message=Enter commit message: "

if "%commit_message%"=="" (
    set "commit_message=GiftAura+ update"
)

"C:\Program Files\Git\cmd\git.exe" commit -m "%commit_message%"

REM ------------------------------------------------------------
REM A commit can fail simply because there are no new changes.
REM We continue because there may still be remote changes to pull.
REM ------------------------------------------------------------

echo.

REM ============================================================
REM 6. SYNC + PUSH
REM ============================================================

echo [6/6] Syncing with GitHub...
echo.

"C:\Program Files\Git\cmd\git.exe" pull origin main --rebase

if errorlevel 1 (
    echo.
    echo ==========================================
    echo        ERROR: GIT PULL / REBASE FAILED
    echo ==========================================
    echo.
    echo There may be a merge conflict.
    echo.
    echo Run:
    echo.
    echo git status
    echo.
    echo Resolve the conflict before running this BAT again.
    echo.
    pause
    exit /b 1
)

echo.
echo GitHub changes synchronized.
echo.

echo Pushing local changes to GitHub...
echo.

"C:\Program Files\Git\cmd\git.exe" push origin main

if errorlevel 1 (
    echo.
    echo ==========================================
    echo             PUSH FAILED
    echo ==========================================
    echo.
    echo GitHub rejected the push.
    echo.
    echo Check the error above.
    echo.
    pause
    exit /b 1
)

REM ============================================================
REM SUCCESS
REM ============================================================

echo.
echo.
echo ==========================================
echo       GITHUB UPDATE SUCCESSFUL
echo ==========================================
echo.
echo Project:
echo GiftAura+
echo.
echo Local folder:
echo D:\Gift
echo.
echo GitHub:
echo https://github.com/nikhilsarojbwr-stack/GiftauraCa2
echo.
echo ==========================================
echo.
echo Your latest GiftAura+ changes are on GitHub.
echo.

pause