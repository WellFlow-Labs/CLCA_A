@echo off
echo ============================================
echo   CLCA 3.3 — FULL PIPELINE REBUILD
echo   Clearing old results and re-running P/F/G
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. CLEAN OLD OUTPUTS
REM ------------------------------------------------------

echo Deleting old data folders...
rmdir /s /q data\ka
rmdir /s /q data\yo
rmdir /s /q data\fi
rmdir /s /q data\eu
rmdir /s /q data\ta
rmdir /s /q data\id
rmdir /s /q data\tr
rmdir /s /q data\ko
rmdir /s /q data\global_set_A
echo Done.
echo.

REM ------------------------------------------------------
REM 2. RUN P+F FOR ALL LANGUAGES (Anthropic)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for all languages
echo ============================================

call python -m src.runners.run_language --language-name "Georgian"    --language-code ka --script Georgian    --backend anthropic
call python -m src.runners.run_language --language-name "Yoruba"      --language-code yo --script Latin       --backend anthropic
call python -m src.runners.run_language --language-name "Finnish"     --language-code fi --script Latin       --backend anthropic
call python -m src.runners.run_language --language-name "Basque"      --language-code eu --script Latin       --backend anthropic
call python -m src.runners.run_language --language-name "Tamil"       --language-code ta --script Tamil       --backend anthropic
call python -m src.runners.run_language --language-name "Indonesian"  --language-code id --script Latin       --backend anthropic
call python -m src.runners.run_language --language-name "Turkish"     --language-code tr --script Latin       --backend anthropic
call python -m src.runners.run_language --language-name "Korean"      --language-code ko --script Hangul      --backend anthropic

echo.
echo === Finished P + F phases ===
echo.

REM ------------------------------------------------------
REM 3. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across languages
echo ============================================

call python -m src.runners.verify_languages configs\global_set_A_codes.toml

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 4. RUN GLOBAL G-PHASE (OpenAI)
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1–G9)
echo ============================================

call python -m src.runners.run_global_analysis ^
  --languages ka yo fi eu ta id tr ko ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_A

echo.
echo ============================================
echo   FULL PIPELINE COMPLETE
echo ============================================
pause
