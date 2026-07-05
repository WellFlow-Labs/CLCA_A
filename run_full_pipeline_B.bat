@echo off
echo ============================================
echo   CLCA 3.3 — FULL PIPELINE REBUILD (Set B)
echo   Clearing old results and re-running P/F/G
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. CLEAN OLD OUTPUTS
REM ------------------------------------------------------

echo Deleting old data folders...
rmdir /s /q data\zh
rmdir /s /q data\he
rmdir /s /q data\sa
rmdir /s /q data\el
rmdir /s /q data\en
rmdir /s /q data\tl
rmdir /s /q data\sw
rmdir /s /q data\qu
rmdir /s /q data\global_set_B
echo Done.
echo.

REM ------------------------------------------------------
REM 2. RUN P+F FOR ALL LANGUAGES (Anthropic)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for Set B languages
echo ============================================

call python -m src.runners.run_language --language-name "Chinese"  --language-code zh --script Han        --backend anthropic
call python -m src.runners.run_language --language-name "Hebrew"   --language-code he --script Hebrew     --backend anthropic
call python -m src.runners.run_language --language-name "Sanskrit" --language-code sa --script Devanagari --backend anthropic
call python -m src.runners.run_language --language-name "Greek"    --language-code el --script Greek      --backend anthropic
call python -m src.runners.run_language --language-name "English"  --language-code en --script Latin      --backend anthropic
call python -m src.runners.run_language --language-name "Tagalog"  --language-code tl --script Latin      --backend anthropic
call python -m src.runners.run_language --language-name "Swahili"  --language-code sw --script Latin      --backend anthropic
call python -m src.runners.run_language --language-name "Quechua"  --language-code qu --script Latin      --backend anthropic

echo.
echo === Finished P + F phases (Set B) ===
echo.

REM ------------------------------------------------------
REM 3. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across Set B
echo ============================================

call python -m src.runners.verify_languages configs\global_set_B_codes.toml

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 4. RUN GLOBAL G-PHASE (Anthropic long-context)
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1–G9) for Set B
echo ============================================

call python -m src.runners.run_global_analysis ^
  --languages zh he sa el en tl sw qu ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_B

echo.
echo ============================================
echo   FULL PIPELINE COMPLETE (Set B)
echo ============================================
pause
