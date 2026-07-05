@echo off
echo ============================================
echo   CLCA -- WITHIN-PROTOCOL REPRODUCIBILITY RERUN (Set A)
echo   Backend: Anthropic / claude-sonnet-4-5 (same as main run)
echo   Output:  data_reproducibility\
echo
echo   Purpose: independent second run of the CLCA-Revision
echo   pipeline on the same 8 Set A languages, for run-to-run
echo   reproducibility analysis against data\. The original
echo   data\ outputs are NOT touched.
echo ============================================
echo.

REM ------------------------------------------------------
REM 1. CLEAN ONLY THE REPRODUCIBILITY OUTPUT FOLDERS
REM    (data\ is never touched here)
REM ------------------------------------------------------

echo Clearing data_reproducibility\ Set A folders only...
rmdir /s /q data_reproducibility\ka
rmdir /s /q data_reproducibility\yo
rmdir /s /q data_reproducibility\fi
rmdir /s /q data_reproducibility\eu
rmdir /s /q data_reproducibility\ta
rmdir /s /q data_reproducibility\id
rmdir /s /q data_reproducibility\tr
rmdir /s /q data_reproducibility\ko
rmdir /s /q data_reproducibility\global_set_A
echo Done.
echo.

REM ------------------------------------------------------
REM 2. RUN P+F FOR ALL SET A LANGUAGES (Anthropic)
REM ------------------------------------------------------

echo ============================================
echo   Running P + F phases for Set A (rerun)
echo ============================================

call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Georgian"    --language-code ka --script Georgian    --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Yoruba"      --language-code yo --script Latin       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Finnish"     --language-code fi --script Latin       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Basque"      --language-code eu --script Latin       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Tamil"       --language-code ta --script Tamil       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Indonesian"  --language-code id --script Latin       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Turkish"     --language-code tr --script Latin       --backend anthropic
call python -m src.runners.run_language --data-dir data_reproducibility --language-name "Korean"      --language-code ko --script Hangul      --backend anthropic

echo.
echo === Finished P + F phases (Set A rerun) ===
echo.

REM ------------------------------------------------------
REM 3. VERIFY COMPLETENESS
REM ------------------------------------------------------

echo ============================================
echo   Verifying completeness across Set A (rerun)
echo ============================================

call python -m src.runners.verify_languages configs\global_set_A_codes.toml --data-dir data_reproducibility

echo.
echo === Verification Complete ===
echo.

REM ------------------------------------------------------
REM 4. RUN GLOBAL G-PHASE
REM ------------------------------------------------------

echo ============================================
echo   Running Global G-phase (G1-G9) for Set A
echo ============================================

call python -m src.runners.run_global_analysis --data-dir data_reproducibility ^
  --languages ka yo fi eu ta id tr ko ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_A

echo.
echo ============================================
echo   REPRODUCIBILITY RERUN COMPLETE (Set A)
echo
echo   Compare against data\ with:
echo     python -m src.runners.compare_runs --baseline data --rerun data_reproducibility --set A
echo ============================================
pause
