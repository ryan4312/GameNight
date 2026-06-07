param(
  [string]$CommitMessage = "Game Night weekly update"
)

python .uild_gamenight_v1_6.py
python .\capture_posters_v1_6.py

git add .
git commit -m $CommitMessage
git push origin main
