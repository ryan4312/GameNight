from pathlib import Path
import json, html

DATA_FILE = Path('weekly-data-v1.6.json')
ROOT = Path('.')
HOOKS_DIR = ROOT / 'hooks'
HOOKS_DIR.mkdir(exist_ok=True)
ASSETS_DIR = ROOT / 'assets' / 'images'
ASSETS_DIR.mkdir(parents=True, exist_ok=True)

def h(text):
    return html.escape(str(text))

def load_data():
    return json.loads(DATA_FILE.read_text(encoding='utf-8'))

def slug_status(status: str):
    s = status.lower().replace('⭐ ', '').replace('?', '')
    for old, new in [(' ', '-'), ('—', '-'), ('–', '-')]:
        s = s.replace(old, new)
    return s

def nav(current):
    items = [('Home', 'index.html'), ('New + Updated', 'new-and-updated.html'), ('Back in Rotation', 'back-in-rotation.html')]
    return '<div class="nav-row">' + ''.join(
        f'<a class="nav-link{" active" if href == current else ""}" href="{href}">{h(label)}</a>'
        for label, href in items
    ) + '</div>'

def page_css(dot_color, dot_shadow):
    return f"""
    :root {{
      --bg:#0d0d14; --ink:#f6f2ea; --muted:#d2cabf; --line:rgba(255,255,255,.11);
      --shadow:0 18px 44px rgba(0,0,0,.34); --new:#39d353; --updated:#5ea0ff;
      --played:#f6c453; --favorite:#f6c453; --unplayed:#ff5d5d;
    }}
    * {{ box-sizing:border-box; }} html, body {{ margin:0; }}
    body {{ color:var(--ink); font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif; background: radial-gradient(circle at top, #25253d 0%, var(--bg) 42%), linear-gradient(180deg, #14121b 0%, #08080b 100%); min-height:100vh; }}
    .shell {{ width:min(1400px, 100%); min-height:100vh; margin:0 auto; padding:42px 56px; position:relative; overflow:hidden; }}
    .shell::before {{ content:''; position:absolute; inset:0; pointer-events:none; opacity:.05; background-image: radial-gradient(circle, rgba(255,255,255,.9) 1px, transparent 1px); background-size:6px 6px; mix-blend-mode:overlay; }}
    .topline {{ display:flex; justify-content:space-between; gap:20px; text-transform:uppercase; letter-spacing:.22em; font-size:15px; color:var(--muted); margin-bottom:16px; position:relative; z-index:2; }}
    .nav-row {{ display:flex; gap:12px; flex-wrap:wrap; margin:8px 0 18px; position:relative; z-index:2; }}
    .nav-link {{ border:1px solid var(--line); border-radius:999px; padding:10px 16px; text-decoration:none; background:rgba(255,255,255,.03); color:var(--muted); font-size:14px; letter-spacing:.12em; text-transform:uppercase; font-weight:700; box-shadow:var(--shadow); }}
    .nav-link.active {{ color:var(--ink); border-color:rgba(255,255,255,.22); background:rgba(255,255,255,.07); }}
    .head {{ margin:8px 0 26px; position:relative; z-index:2; }}
    .kicker {{ color:#f1d48b; text-transform:uppercase; letter-spacing:.22em; font-weight:700; font-size:18px; margin-bottom:10px; }}
    h1 {{ margin:0; font-size:112px; line-height:.92; letter-spacing:-.045em; text-transform:uppercase; max-width:1120px; }}
    .subtitle {{ max-width:980px; margin-top:18px; font-size:28px; line-height:1.28; color:var(--muted); }}
    .rule {{ height:1px; background: linear-gradient(90deg, var(--line), transparent); margin:26px 0; }}
    .section-label {{ display:inline-flex; align-items:center; gap:12px; margin-bottom:24px; font-size:22px; font-weight:800; text-transform:uppercase; letter-spacing:.14em; position:relative; z-index:2; }}
    .section-label .dot {{ width:16px; height:16px; border-radius:999px; background:{dot_color}; box-shadow:0 0 0 8px {dot_shadow}; }}
    .grid {{ display:grid; grid-template-columns:repeat(3,1fr); gap:22px; position:relative; z-index:2; }}
    .tile {{ position:relative; display:block; min-height:360px; overflow:hidden; border-radius:18px; text-decoration:none; color:inherit; border:1px solid var(--line); background:linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02)); box-shadow:var(--shadow); }}
    .tile.highlight {{ min-height:430px; }} .tile.updated-block {{ outline:2px solid rgba(94,160,255,.78); outline-offset:-2px; }}
    .img-wrap {{ position:absolute; inset:0; background:linear-gradient(180deg, #1d2432, #101018); }}
    img {{ width:100%; height:100%; object-fit:cover; display:block; max-width:100%; }}
    .shade {{ position:absolute; inset:0; background:linear-gradient(180deg, rgba(0,0,0,.03), rgba(0,0,0,.26) 55%, rgba(0,0,0,.92)); }}
    .meta {{ position:absolute; left:18px; right:18px; bottom:16px; z-index:2; }}
    .chip {{ display:inline-block; margin-bottom:12px; padding:7px 11px; border-radius:999px; font-size:13px; font-weight:900; text-transform:uppercase; letter-spacing:.1em; background:rgba(12,12,17,.75); border:1px solid rgba(255,255,255,.18); backdrop-filter:blur(10px); }}
    .chip.new {{ color:var(--new); border-color:rgba(57,211,83,.5); }}
    .chip.updated {{ color:var(--updated); border-color:rgba(94,160,255,.5); }}
    .chip.briefly-played {{ color:var(--played); border-color:rgba(246,196,83,.45); }}
    .chip.previous-favorite {{ color:var(--favorite); border-color:rgba(246,196,83,.45); }}
    .chip.unplayed {{ color:var(--unplayed); border-color:rgba(255,93,93,.5); }}
    .meta h3 {{ margin:0; font-size:36px; line-height:1.03; letter-spacing:-.03em; text-shadow:0 3px 12px rgba(0,0,0,.5); }}
    .bottom-nav {{ display:flex; justify-content:space-between; gap:16px; margin-top:34px; padding-top:16px; border-top:1px solid var(--line); position:relative; z-index:2; }}
    .bottom-nav .group {{ display:flex; gap:12px; flex-wrap:wrap; }}
    .hero-wrap {{ display:grid; grid-template-columns:140px 1fr; gap:24px; align-items:center; position:relative; z-index:2; }}
    .brand-icon {{ width:128px; height:128px; border-radius:26px; display:block; box-shadow:var(--shadow); border:1px solid rgba(255,255,255,.14); object-fit:cover; }}
    .grid-home {{ display:grid; grid-template-columns:1.1fr .9fr; gap:26px; position:relative; z-index:2; margin-top:28px; }}
    .card {{ border:1px solid var(--line); border-radius:22px; background:linear-gradient(180deg, rgba(255,255,255,.06), rgba(255,255,255,.02)); box-shadow:var(--shadow); padding:24px; }}
    .card h2 {{ margin:0 0 12px; font-size:40px; line-height:1; text-transform:uppercase; letter-spacing:-.03em; }}
    .card p {{ margin:0; color:var(--muted); font-size:22px; line-height:1.4; }}
    .link-stack {{ display:grid; gap:16px; margin-top:18px; }}
    .poster-link {{ display:block; border:1px solid var(--line); border-radius:18px; padding:18px; text-decoration:none; background:rgba(255,255,255,.03); color:inherit; }}
    .poster-link .eyebrow {{ color:var(--muted); text-transform:uppercase; letter-spacing:.16em; font-size:14px; font-weight:700; }}
    .poster-link h3 {{ margin:8px 0 8px; font-size:36px; line-height:1.02; letter-spacing:-.03em; text-transform:uppercase; }}
    .poster-link p {{ margin:0; color:var(--muted); font-size:20px; line-height:1.35; }}
    .buttons {{ display:flex; gap:12px; flex-wrap:wrap; margin-top:20px; }}
    .button {{ display:inline-flex; border-radius:999px; padding:12px 18px; text-decoration:none; text-transform:uppercase; letter-spacing:.14em; font-size:14px; font-weight:800; border:1px solid var(--line); }}
    .button.primary {{ background:rgba(57,211,83,.12); border-color:rgba(57,211,83,.45); color:#cbffd2; }}
    .button.secondary {{ background:rgba(94,160,255,.11); border-color:rgba(94,160,255,.4); color:#d9e7ff; }}
    .event-box {{ margin-top:18px; padding:18px; border:1px solid rgba(255,255,255,.12); border-radius:18px; background:rgba(255,255,255,.03); }}
    @media (max-width: 1200px) {{ .shell {{ padding:28px 24px; }} h1 {{ font-size:84px; max-width:100%; }} .subtitle {{ font-size:24px; max-width:100%; }} .grid {{ grid-template-columns:repeat(2,1fr); }} .grid-home {{ grid-template-columns:1fr; }} .tile.highlight {{ min-height:380px; }} .card h2 {{ font-size:34px; }} }}
    @media (max-width: 800px) {{ .topline {{ font-size:12px; letter-spacing:.16em; }} .nav-row, .bottom-nav, .bottom-nav .group {{ gap:8px; }} .nav-link {{ padding:9px 12px; font-size:12px; }} .hero-wrap {{ grid-template-columns:1fr; gap:18px; }} .brand-icon {{ width:96px; height:96px; border-radius:22px; }} .kicker {{ font-size:14px; }} h1 {{ font-size:54px; line-height:.98; }} .subtitle {{ font-size:18px; line-height:1.45; }} .section-label {{ font-size:16px; }} .grid {{ grid-template-columns:1fr; gap:16px; }} .tile, .tile.highlight {{ min-height:300px; }} .meta h3 {{ font-size:28px; }} .card {{ padding:18px; }} .card h2 {{ font-size:28px; }} .card p, .poster-link p {{ font-size:18px; }} .poster-link h3 {{ font-size:28px; }} .button {{ font-size:12px; padding:10px 14px; }} .bottom-nav {{ flex-direction:column; align-items:stretch; }} .bottom-nav .group {{ justify-content:flex-start; }} }}
    @media (max-width: 480px) {{ .shell {{ padding:18px 14px; }} .topline {{ flex-direction:column; gap:6px; }} h1 {{ font-size:40px; }} .subtitle {{ font-size:16px; }} .brand-icon {{ width:80px; height:80px; border-radius:18px; }} .meta {{ left:14px; right:14px; bottom:12px; }} .meta h3 {{ font-size:24px; }} .chip {{ font-size:11px; padding:6px 9px; }} .tile, .tile.highlight {{ min-height:260px; }} .card h2 {{ font-size:24px; }} .card p, .poster-link p {{ font-size:16px; }} .poster-link h3 {{ font-size:24px; }} .poster-link .eyebrow {{ font-size:12px; }} .buttons {{ gap:8px; }} }}
    """

def tile(game):
    classes = ['tile']
    if game.get('highlight'):
        classes.append('highlight')
    if game.get('status') == 'UPDATED':
        classes.append('updated-block')
    return f'<a class="{" ".join(classes)}" href="{game["steam_url"]}" target="_blank" rel="noreferrer"><div class="img-wrap"><img loading="eager" decoding="async" src="{game["cover_url"]}" alt="{h(game["title"])} cover art"><div class="shade"></div></div><div class="meta"><span class="chip {slug_status(game["status"])}">{h(game["status"])}</span><h3>{h(game["title"])}</h3></div></a>'

def make_index(data):
    site, copy = data['site'], data['copy']
    return f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>{h(copy["home_title"])}</title><style>{page_css("#39d353","rgba(57,211,83,.13)")}</style></head><body><main class="shell"><div class="topline"><div>Wednesday • Game Night</div><div>Homepage</div></div>{nav("index.html")}<section class="head hero-wrap"><img class="brand-icon" src="{site["brand_icon_path"]}" alt="Game Night branding icon"><div><div class="kicker">{h(copy["home_kicker"])}</div><h1>{h(copy["home_title"])}</h1><div class="subtitle">{h(copy["home_description"])}</div></div></section><section class="grid-home"><div class="card"><h2>What It Is</h2><p>Game Night is the weekly landing spot for the current lineup. Use the two linked pages to browse the visual poster set for this week’s new additions, updates, previous favorites, and anything still waiting for a proper session.</p><div class="event-box"><h2 style="font-size:28px; margin:0 0 8px;">Discord Event</h2><p style="font-size:20px;">Use the event page to RSVP and jump straight into the Wednesday plan.</p><div class="buttons"><a class="button primary" href="{site["event_url"]}">Open Discord Event</a></div></div></div><div class="card"><h2>This Week</h2><div class="link-stack"><a class="poster-link" href="new-and-updated.html"><div class="eyebrow">Poster Page</div><h3>New + Updated</h3><p>{h(copy["new_subtitle"])}</p></a><a class="poster-link" href="back-in-rotation.html"><div class="eyebrow">Poster Page</div><h3>Back in Rotation</h3><p>{h(copy["rotation_subtitle"])}</p></a></div><div class="buttons"><a class="button primary" href="new-and-updated.html">Open New + Updated</a><a class="button secondary" href="back-in-rotation.html">Open Back in Rotation</a></div></div></section></main></body></html>'

def make_page(data, page_title, subtitle, label, games, current, dot, shadow):
    tiles = ''.join(tile(g) for g in games)
    event_url = data['site']['event_url']
    return f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" /><title>{h(page_title)}</title><style>{page_css(dot, shadow)}</style></head><body><main class="shell"><div class="topline"><div>Wednesday • Game Night</div><div>{h(page_title)}</div></div>{nav(current)}<header class="head"><div class="kicker">This Week\'s Games</div><h1>{h(page_title)}</h1><div class="subtitle">{h(subtitle)}</div></header><div class="rule"></div><div class="section-label"><span class="dot"></span>{h(label)}</div><section class="grid">{tiles}</section><div class="bottom-nav"><div class="group"><a class="nav-link" href="index.html">Home</a><a class="nav-link" href="new-and-updated.html">New + Updated</a><a class="nav-link" href="back-in-rotation.html">Back in Rotation</a></div><div class="group"><a class="nav-link" href="{event_url}">Discord Event</a></div></div></main></body></html>'

def make_markdown(data):
    site, copy = data['site'], data['copy']
    lines = ['🎮 **Wednesday Game Night**', f'**{copy["discord_intro"]}**', '🟢 **NEW THIS WEEK**']
    lines += [f'• [{g["title"]}]({g["steam_url"]})' for g in data['games']['new']]
    lines += ['🔄 **UPDATED**']
    lines += [f'• [{g["title"].replace("?","")}]({g["steam_url"]})' for g in data['games']['updated']]
    lines += ['🔁 **BACK IN ROTATION**']
    for g in data['games']['rotation']:
        status = g['status'].replace('⭐ PREVIOUS FAVORITE', '⭐ favorite').replace('BRIEFLY PLAYED', 'briefly played').replace('UNPLAYED', 'unplayed')
        lines.append(f'• [{g["title"]}]({g["steam_url"]}) — _{status.lower()}_')
    lines += ['', '#### ✨ Find out more here:', '', f'[**{site["site_url"]}new-and-updated.html**]({site["site_url"]}new-and-updated.html)']
    return '\n'.join(lines) + '\n'

def make_standard_json(data):
    site, copy = data['site'], data['copy']
    new_lines = '\\n'.join([f'> • [{g["title"]}]({g["steam_url"]})' for g in data['games']['new']])
    upd_lines = '\\n'.join([f'> • [{g["title"].replace("?","")}]({g["steam_url"]})' for g in data['games']['updated']])
    rot_lines = []
    for g in data['games']['rotation']:
        status = g['status'].replace('⭐ PREVIOUS FAVORITE', '⭐ *favorite*').replace('BRIEFLY PLAYED', '*briefly played*').replace('UNPLAYED', '*unplayed*')
        rot_lines.append(f'> • [{g["title"]}]({g["steam_url"]}) — {status}')
    payload = {
        'username': site['name'], 'avatar_url': site['avatar_url'],
        'content': f'🎮 **Wednesday Game Night**\\n> **{copy["discord_intro"]}**\\n\\n🟢 **NEW THIS WEEK**\\n{new_lines}\\n\\n🔄 **UPDATED**\\n{upd_lines}\\n\\n🔁 **BACK IN ROTATION**\\n' + '\\n'.join(rot_lines) + f'\\n\\n> ### ✨ Find out more here:\\n> **{site["site_url"]}new-and-updated.html**',
        'embeds': [
            {'url': 'https://discohook.app', 'color': 5814783, 'image': {'url': site['new_poster_image']}, 'fields': [{'name': 'TL;DR: Here are two posters with everything new, updated, and back in rotation this week.', 'value': ''}]},
            {'url': 'https://discohook.app', 'image': {'url': site['rotation_poster_image']}}
        ], 'components': []
    }
    return json.dumps(payload, indent=2)

def make_compact_json(data):
    site, copy = data['site'], data['copy']
    new_value = '\\n'.join([f'> • [{g["title"]}]({g["steam_url"]})' for g in data['games']['new']])
    rot_value = '\\n'.join([f'> • [{g["title"]}]({g["steam_url"]}){" ⭐" if "FAVORITE" in g["status"] else ""}' for g in data['games']['rotation']])
    upd_value = '\\n'.join([f'> • [{g["title"].replace("?","")}]({g["steam_url"]})' for g in data['games']['updated']])
    payload = {
        'username': site['name'], 'avatar_url': site['avatar_url'],
        'embeds': [
            {'title': '🎮 **Wednesday Game Night**', 'description': f'> **{copy["discord_intro"]}**', 'url': site['event_url'], 'color': 15277667, 'image': {'url': site['new_poster_image']}, 'fields': [
                {'name': '🟢 **NEW THIS WEEK**', 'value': new_value, 'inline': True}, {'name': '🔁 **BACK IN ROTATION**', 'value': rot_value, 'inline': True}, {'name': '🔄 **UPDATED**', 'value': upd_value, 'inline': False}
            ]},
            {'url': site['event_url'], 'image': {'url': site['rotation_poster_image']}}
        ],
        'components': [{'type': 1, 'components': [{'type': 2, 'style': 5, 'label': '✨ Find out more here:', 'url': site['site_url'] + 'new-and-updated.html', 'custom_id': 'game_night_more_info'}]}]
    }
    return json.dumps(payload, indent=2)

def main():
    data = load_data()
    Path('index.html').write_text(make_index(data), encoding='utf-8')
    Path('new-and-updated.html').write_text(make_page(data, 'New + Updated', data['copy']['new_subtitle'], 'New This Week + Updated', data['games']['new'] + data['games']['updated'], 'new-and-updated.html', '#39d353', 'rgba(57,211,83,.13)'), encoding='utf-8')
    Path('back-in-rotation.html').write_text(make_page(data, 'Back in Rotation', data['copy']['rotation_subtitle'], 'Back in Rotation', data['games']['rotation'], 'back-in-rotation.html', '#ff6b46', 'rgba(255,107,70,.13)'), encoding='utf-8')
    Path('discord_game_night_post.md').write_text(make_markdown(data), encoding='utf-8')
    Path('hooks/GameNight-WeeklyUpdate-Standard.json').write_text(make_standard_json(data), encoding='utf-8')
    Path('hooks/GameNight-WeeklyUpdate-Compact.json').write_text(make_compact_json(data), encoding='utf-8')
    print('Generated all v1.6 outputs.')

if __name__ == '__main__':
    main()
