@echo off
setlocal enabledelayedexpansion
set count=1
for /f "tokens=* delims=" %%a in ('dir /a-d/b/s "*.py"') do (
    if !count! leq 5 (
        start "" python "%%a"
        set /A count+=1
    ) else (
        ping localhost -n 5 >nul
        start "" python "%%a"
        set count=1
    )
)
pause
exit