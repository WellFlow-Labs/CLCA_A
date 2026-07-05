@echo off
echo ============================================
echo   CLCA 3.3 -- FULL PIPELINE (GPT-5.4, Set A)
echo   Output goes to data_gpt54\
echo   Requires: openai>=1.66.0, OPENAI_API_KEY
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. RUN P+F FOR ALL LANGUAGES (GPT-5.4)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for all languages
echo ============================================

call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Georgian"    --language-code ka --script Georgian
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Yoruba"      --language-code yo --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Finnish"     --language-code fi --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Basque"      --language-code eu --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Tamil"       --language-code ta --script Tamil
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Indonesian"  --language-code id --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Turkish"     --language-code tr --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Korean"      --language-code ko --script Hangul

echo.
echo === Finished P + F phases ===
echo.

REM ------------------------------------------------------
REM 2. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across languages
echo ============================================

call python -m src.runners.verify_languages configs\global_set_A_codes.toml --data-dir data_gpt54

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 3. RUN GLOBAL G-PHASE (GPT-5.4 long-context)
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1-G9)
echo ============================================

call python -m src.runners.run_global_analysis --config src/config/settings_gpt54.toml --data-dir data_gpt54 ^
  --languages ka yo fi eu ta id tr ko ^
  --output-code global_set_A

echo.
echo ============================================
echo   FULL PIPELINE COMPLETE (GPT-5.4, Set A)
echo ============================================
pause
