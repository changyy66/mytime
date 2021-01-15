@echo off
set PATH=%PATH%%~dp0;
echo %PATH%

REG ADD "HKLM\SYSTEM\controlset001\Control\Session Manager\Environment" /v "Path" /t REG_EXPAND_SZ /d "%PATH%"
pause