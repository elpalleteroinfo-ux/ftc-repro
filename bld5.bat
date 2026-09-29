@echo off
#Test bat file
robocopy "%SRC_DIR%\src" "%SP_DIR%" /E
if %errorlevel% LEQ 4 (
    exit /b 0
) else (
    exit /b %errorlevel%
)

mkdir /p "${PREFIX}\share\systemd\user"
robocopy "%SRC_DIR%\systemd" "%PREFIX%\share\systemd\user" /E
if %errorlevel% LEQ 4 (
    exit /b 0
) else (
    exit /b %errorlevel%
)

mkdir /p "${PREFIX}\share\UnifiedMETDownloader"
robocopy "%SRC_DIR%\config" "%PREFIX%\share\UnifiedMETDownloader" /E
if %errorlevel% LEQ 4 (
    exit /b 0
) else (
    exit /b %errorlevel%
)
