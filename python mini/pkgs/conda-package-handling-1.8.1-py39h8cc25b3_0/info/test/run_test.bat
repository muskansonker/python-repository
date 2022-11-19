



pytest tests -k "not test_secure_refusal_to_extract_abs_paths"
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
