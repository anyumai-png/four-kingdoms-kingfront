#!/usr/bin/env python3
import json
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
RUNS=12
SECONDS=600
UNIT_CAP=140
ARROW_CAP=180
FX_CAP=160

def main():
    html=(ROOT/'index.html').read_text(encoding='utf-8')
    rows=[]
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox','--disable-dev-shm-usage'])
        try:
            for i in range(RUNS):
                page=browser.new_page(viewport={'width':844,'height':390}, is_mobile=True, has_touch=True, device_scale_factor=3)
                errors=[]
                page.on('pageerror', lambda exc, bucket=errors: bucket.append(str(exc)))
                page.set_content(html, wait_until='load')
                page.evaluate('window.__KINGFRONT_DEBUG__.start()')
                state=page.evaluate(f'window.__KINGFRONT_DEBUG__.step({SECONDS})')
                kings=state['kings']
                player_alive=bool(kings[0]['alive'])
                enemy_alive=sum(1 for k in kings[1:] if k['alive'])
                auto_victory=bool(state['over'] and player_alive and enemy_alive==0)
                row={
                    'run':i+1,
                    'over':bool(state['over']),
                    'player_alive':player_alive,
                    'enemy_alive':enemy_alive,
                    'auto_victory':auto_victory,
                    'units':state['units'],
                    'arrows':state['arrows'],
                    'fx':state['fx'],
                    'tech':state.get('tech',[]),
                    'tech_buys':state.get('techBuys',[]),
                    'errors':errors,
                }
                rows.append(row)
                page.close()
        finally:
            browser.close()
    out=ROOT/'tests'/'monte_carlo_last.json'
    out.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    runtime_errors=sum(bool(r['errors']) for r in rows)
    auto_victories=sum(r['auto_victory'] for r in rows)
    cap_failures=sum(r['units']>UNIT_CAP or r['arrows']>ARROW_CAP or r['fx']>FX_CAP for r in rows)
    player_deaths=sum(not r['player_alive'] for r in rows)
    maxima={k:max(r[k] for r in rows) for k in ('units','arrows','fx')}
    ai_tech_totals=[sum(sum(team.values()) for team in r.get('tech',[])[1:]) for r in rows]
    tech_level_failures=sum(any(any(level<0 or level>3 for level in team.values()) for team in r.get('tech',[])) for r in rows)
    no_ai_research=sum(total==0 for total in ai_tech_totals)
    print(f'Monte Carlo {RUNS}x{SECONDS}s: runtime_errors={runtime_errors} auto_victories={auto_victories} player_deaths={player_deaths} cap_failures={cap_failures} tech_level_failures={tech_level_failures} no_ai_research={no_ai_research} ai_tech_range=({min(ai_tech_totals)},{max(ai_tech_totals)}) maxima={maxima}')
    if runtime_errors or auto_victories or cap_failures or tech_level_failures or no_ai_research:
        return 1
    return 0

if __name__=='__main__':
    raise SystemExit(main())
