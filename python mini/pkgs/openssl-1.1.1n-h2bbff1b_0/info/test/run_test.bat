



copy NUL checksum.txt
IF %ERRORLEVEL% NEQ 0 exit /B 1
openssl sha256 checksum.txt
IF %ERRORLEVEL% NEQ 0 exit /B 1
python -c "import certifi; import ssl; import urllib.request as urlrq; urlrq.urlopen('https://pypi.org', context=ssl.create_default_context(cafile=certifi.where()))"
IF %ERRORLEVEL% NEQ 0 exit /B 1
exit /B 0
