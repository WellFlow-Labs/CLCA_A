@echo off
echo ============================================
echo   CLCA -- WITHIN-PROTOCOL REPRODUCIBILITY RERUN (Set B)
echo   Backend: Anthropic / claude-sonnet-4-5 (same as main run)
echo   Output:  data_reproducibility\
echo
echo   Purpose: independent second run of the CLCA-Revision
echo   pipeline on the same 8 Set B languages, for run-to-run
echo   reproducibility analysis against data\. The original
echo   data\ outputs are NOT touched.
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. CLEAN ONLY THE REPRODUCIBILITY OUTPUT FOLDERS
REM    (data\ is never touched here)
REM ------------------------------------------------------

echo Clearing data_reproducibility\ Set B folders only...
rmdir /s /q data_reproducibility\zh
rmdir /s /q data_reproducibility\he
rmdir /s /q data_reproducibility\sa
rmdir /s /q data_reproducibility\el
rmdir /s /q data_reproducibility\en
rmdir /s /q data_reproducibility\tl
rmdir /s /q data_reproducibility\sw
rmdir /s /q data_reproducibility\qu
rmdir /s /q data_reproducibility\global_set_B
echo Done.
echo.

REM ------------------------------------------------------
REM 2. RUN P+F FOR ALL SET B LANGUAGES (Anthropic)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for Set B (rerun)
echo ============================================

call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Chinese"  --language-code zh --script Han        --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Hebrew"   --language-code he --script Hebrew     --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Sanskrit" --language-code sa --script Devanagari --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Greek"    --language-code el --script Greek      --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "English"  --language-code en --script Latin      --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Tagalog"  --language-code tl --script Latin      --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Swahili"  --language-code sw --script Latin      --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Quechua"  --language-code qu --script Latin      --backend anthropic

echo.
echo === Finished P + F phases (Set B rerun) ===
echo.

REM ------------------------------------------------------
REM 3. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across Set B (rerun)
echo ============================================

call python -m src.runners.verify_languages configs\global_set_B_codes.toml --data-dir data_reproducibility

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 4. RUN GLOBAL G-PHASE
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1-G9) for Set B
echo ============================================

call python -m src.runners.run_global_analysis --data-dir data_reproducibility ^
  --languages zh he sa el en tl sw qu ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_B

echo.
echo ============================================
echo   REPRODUCIBILITY RERUN COMPLETE (Set B)
echo
echo   Compare against data\ with:
echo     python -m src.runners.compare_runs --baseline data --rerun data_reproducibility --set B
echo ============================================
pause
