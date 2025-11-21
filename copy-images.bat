@echo off
REM Batch script to copy city images to the project

echo ============================================
echo  Copy City Images to MedSpa Flywheel
echo ============================================
echo.

REM Get the directory where this script is located
set "PROJECT_DIR=%~dp0"

echo Project directory: %PROJECT_DIR%
echo.

REM Create images\cities directory if it doesn't exist
echo Creating images\cities directory...
if not exist "%PROJECT_DIR%images\cities" (
    mkdir "%PROJECT_DIR%images\cities"
    echo   Created: images\cities
) else (
    echo   Already exists: images\cities
)
echo.

REM Copy the images
echo Copying images from Image_Scraper...
set "SOURCE=C:\Users\james\Image_Scraper\images\cities\*.jpg"
set "DEST=%PROJECT_DIR%images\cities\"

if exist "%SOURCE%" (
    copy "%SOURCE%" "%DEST%" >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        echo   Success: Copied JPG files
    ) else (
        echo   ERROR: Failed to copy files
        echo   Make sure the source path exists:
        echo   %SOURCE%
        pause
        exit /b 1
    )
) else (
    echo   ERROR: Source directory not found:
    echo   %SOURCE%
    echo.
    echo   Please verify the path is correct.
    pause
    exit /b 1
)
echo.

REM Count the files
echo Verifying copied files...
for /f %%A in ('dir /b "%DEST%*.jpg" 2^>nul ^| find /c /v ""') do set COUNT=%%A
echo   Found %COUNT% image files in destination
echo.

if "%COUNT%"=="44" (
    echo SUCCESS: All 44 images copied!
    echo.
    echo Next steps:
    echo   1. Run: python3 scripts/update-city-images.py
    echo   2. Test locally: npm run dev
    echo   3. Commit and push to deploy
) else (
    echo WARNING: Expected 44 images, but found %COUNT%
    echo Please check the source directory.
)

echo.
echo ============================================
pause
