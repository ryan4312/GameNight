@echo off
set MSG=%~1
if "%MSG%"=="" set MSG=Game Night weekly update

python build_gamenight_v1_6.py
python capture_posters_v1_6.py

git add .
git commit -m "%MSG%"
git push origin main
