@echo off
echo ============================================
echo   CLCA -- G-phase only on data_reproducibility\
echo   Use this if the P+F+G batch file got interrupted
echo   after P+F but before G completed.
echo
echo   Reads existing P/F outputs from data_reproducibility\<lang>\
echo   and writes G-phase to data_reproducibility\global_set_A
echo   and data_reproducibility\global_set_B.
echo ============================================
echo.

REM ------------------------------------------------------
REM Clean only the global folders to allow re-running
REM ------------------------------------------------------
echo Clearing data_reproducibility\global_set_A\ ...
rmdir /s /q data_reproducibility\global_set_A
echo Clearing data_reproducibility\global_set_B\ ...
rmdir /s /q data_reproducibility\global_set_B
echo Done.
echo.

REM ------------------------------------------------------
REM Set A G-phase (G1-G9)
REM ------------------------------------------------------
echo ============================================
echo   Running G-phase for Set A
echo ============================================
call python -m src.runners.run_global_analysis --data-dir data_reproducibility ^
  --languages ka yo fi eu ta id tr ko ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_A
echo.
echo === Finished G-phase Set A ===
echo.

REM ------------------------------------------------------
REM Set B G-phase (G1-G9)
REM ------------------------------------------------------
echo ============================================
echo   Running G-phase for Set B
echo ============================================
call python -m src.runners.run_global_analysis --data-dir data_reproducibility ^
  --languages zh he sa el en tl sw qu ^
  --backend anthropic ^
  --model-name claude-sonnet-4-5 ^
  --output-code global_set_B
echo.
echo === Finished G-phase Set B ===
echo.

echo ============================================
echo   G-PHASE RERUN COMPLETE
echo
echo   Next: compare G-phase findings against baseline with:
echo     python -m src.runners.compare_g_phase --baseline data --rerun data_reproducibility
echo ============================================
pause
