 @echo off
 
::現在のディレクトリを取得 
set SCRIPT_DIR=%~dp0

::ポータブルpython.exeのパスを環境変数に追加
set PATH=%PATH%;%SCRIPT_DIR%python-3.7.3-embed-amd64\

::モジュール利用のために、今いるディレクトリのパスを環境変数に追加
set PATH=%PATH%;%SCRIPT_DIR%


