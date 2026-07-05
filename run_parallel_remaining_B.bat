@echo off
echo ============================================
echo   CLCA — Parallel P+I+F for Remaining Set B
echo   Languages: sa, el, en, tl, sw, qu
echo ============================================
echo.

REM Launch 6 languages in parallel (background processes)
echo Starting Sanskrit in background...
start /b cmd /c "python -m src.runners.run_language --language-name Sanskrit --language-code sa --script Devanagari --backend anthropic > logs\sa.log 2>&1"

echo Starting Greek in background...
start /b cmd /c "python -m src.runners.run_language --language-name Greek --language-code el --script Greek --backend anthropic > logs\el.log 2>&1"

echo Starting English in background...
start /b cmd /c "python -m src.runners.run_language --language-name English --language-code en --script Latin --backend anthropic > logs\en.log 2>&1"

echo Starting Tagalog in background...
start /b cmd /c "python -m src.runners.run_language --language-name Tagalog --language-code tl --script Latin --backend anthropic > logs\tl.log 2>&1"

echo Starting Swahili in background...
start /b cmd /c "python -m src.runners.run_language --language-name Swahili --language-code sw --script Latin --backend anthropic > logs\sw.log 2>&1"

echo Starting Quechua in background...
start /b cmd /c "python -m src.runners.run_language --language-name Quechua --language-code qu --script Latin --backend anthropic > logs\qu.log 2>&1"

echo.
echo ============================================
echo   All 6 languages running in parallel!
echo   Check progress: tail -f logs\*.log
echo ============================================
echo.
echo Waiting for all processes to complete...
echo (This may take 30-60 minutes)
echo.

REM Wait for all background processes to finish
:wait_loop
timeout /t 30 /nobreak > nul
tasklist /fi "IMAGENAME eq python.exe" | find "python.exe" > nul
if %errorlevel% equ 0 (
    echo Still running... checking again in 30s
    goto wait_loop
)

echo.
echo ============================================
echo   All languages complete! Verifying...
echo ============================================
call python -m src.runners.verify_languages configs\global_set_B_codes.toml

echo.
echo ============================================
echo   Running Global G-phase (G1-G9)
echo ============================================
call python -m src.runners.run_global_analysis --languages zh he sa el en tl sw qu --backend anthropic --model-name claude-sonnet-4-5 --output-code global_set_B

echo.
echo ============================================
echo   PIPELINE COMPLETE!
echo ============================================
pause
