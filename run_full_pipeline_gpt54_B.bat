@echo off
echo ============================================
echo   CLCA 3.3 -- FULL PIPELINE (GPT-5.4, Set B)
echo   Output goes to data_gpt54\
echo   Requires: openai>=1.66.0, OPENAI_API_KEY
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. RUN P+F FOR ALL LANGUAGES (GPT-5.4)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for Set B languages
echo ============================================

call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Chinese"  --language-code zh --script Han
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Hebrew"   --language-code he --script Hebrew
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Sanskrit" --language-code sa --script Devanagari
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Greek"    --language-code el --script Greek
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "English"  --language-code en --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Tagalog"  --language-code tl --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Swahili"  --language-code sw --script Latin
call python -m src.runners.run_language --config src/config/settings_gpt54.toml --data-dir data_gpt54 --language-name "Quechua"  --language-code qu --script Latin

echo.
echo === Finished P + F phases (Set B) ===
echo.

REM ------------------------------------------------------
REM 2. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across Set B
echo ============================================

call python -m src.runners.verify_languages configs\global_set_B_codes.toml --data-dir data_gpt54

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 3. RUN GLOBAL G-PHASE (GPT-5.4 long-context)
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1-G9) for Set B
echo ============================================

call python -m src.runners.run_global_analysis --config src/config/settings_gpt54.toml --data-dir data_gpt54 ^
  --languages zh he sa el en tl sw qu ^
  --output-code global_set_B

echo.
echo ============================================
echo   FULL PIPELINE COMPLETE (GPT-5.4, Set B)
echo ============================================
pause
