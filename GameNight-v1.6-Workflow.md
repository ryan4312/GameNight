# Game Night v1.6 Workflow

## Single source of truth
Edit only:
- `weekly-data-v1.6.json`

## Build outputs
Running `python build_gamenight_v1_6.py` regenerates:
- `index.html`
- `new-and-updated.html`
- `back-in-rotation.html`
- `discord_game_night_post.md`
- `hooks/GameNight-WeeklyUpdate-Standard.json`
- `hooks/GameNight-WeeklyUpdate-Compact.json`

## Poster screenshots
Running `python capture_posters_v1_6.py` saves updated screenshots to:
- `assets/images/new-and-updated.png`
- `assets/images/back-in-rotation.png`

## Publish
### PowerShell
```powershell
.\publish_gamenight_v1_6.ps1 -CommitMessage "Game Night 2026-06-10"
```

### Command Prompt
```bat
publish_gamenight_v1_6.bat "Game Night 2026-06-10"
```

## Suggested weekly process
1. Edit `weekly-data-v1.6.json`
2. Run the publish script
3. Open the generated JSON in Discohook
4. Send to the announcement channel
