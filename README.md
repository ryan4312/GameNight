# Game Night

GitHub Pages site for the weekly **Game Night** lineup:

**Live site:** https://ryan4312.github.io/GameNight/

## Pages

- `index.html` — homepage / landing page
- `new-and-updated.html` — new games and updates
- `back-in-rotation.html` — previous favorites, briefly played games, and unplayed picks
- `discord_game_night_post.md` — Discord-ready weekly post copy for internal use

## Assets

- `CoolGuysOnly_CGO_Discord_Server_Image.webp` — branding icon used on the homepage

## Publishing on GitHub Pages

This repo is designed to be hosted at:

`https://ryan4312.github.io/GameNight/`

Because the site uses plain relative links, it will work correctly from the repository root when GitHub Pages is enabled.

## Updating the lineup

1. Edit the game titles, statuses, and Steam links in:
   - `new-and-updated.html`
   - `back-in-rotation.html`
   - `discord_game_night_post.md`
2. Commit the changes to GitHub.
3. GitHub Pages will publish the update automatically.

## Discord Event

Homepage event button points to:

https://discord.com/events/1200900538288590898/1339359975687852042

## Notes

- The lineup pages use Steam-hosted cover art with multiple fallback image sources.
- If a Steam image ever stops loading cleanly, adjust the preferred asset order in the page source for that specific game.
