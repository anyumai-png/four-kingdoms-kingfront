# Four Kingdoms — Kingfront Product Specification

## Product vision
A four-kingdom real-time battlefield/tower-defense game. The player is one king who personally enters the battlefield, captures strategic locations, builds and upgrades arrow towers, rallies troops, conducts sieges, and wins by killing the other three kings.

## Core loop
1. Leave the home castle as the king.
2. Capture strategic points personally.
3. Use captured points to grow economy and defense.
4. Build/upgrade arrow towers.
5. Rally a combined-arms field army.
6. Contest territory against three autonomous kingdoms.
7. Break enemy castle defenses: point towers, guard towers, gate.
8. Kill all three enemy kings.

## Loss condition
The player king dies.

## Current gameplay systems
- Four autonomous kingdoms in free-for-all conflict.
- Seven strategic capture points with differentiated bonuses.
- Unit classes: swordsman, shield, archer, cavalry, battering ram.
- Combined-arms roles: shield ranged mitigation, cavalry charge, archer close-range kiting, battering-ram ranged armor and structure priority.
- Player abilities: directional melee attack, Rally/Siege Order, War Cry, Royal Dash.
- Buildable upgradable arrow towers (Lv.1–Lv.3).
- Match-level Royal Armory progression: Shield, Archer, Cavalry, and Siege research paths (Lv.0–Lv.3), paid with battle gold and applied immediately to existing/future troops.
- AI kingdoms use the same research system with personality-led priorities and tactical gold reserves.
- Compact enemy-armory intelligence in the enemy-king HUD exposes rival Shield/Archer/Cavalry/Siege research levels.
- Enemy research completion emits a rate-limited, non-modal battle-feed intelligence event so rival power increases are noticeable without interrupting combat.
- Battlefield-aware Royal Armory advisor recommends one research path with an explainable reason based on enemy ranged pressure, siege phase, weakened kings, and current research levels; recommendations never auto-spend gold.
- The HUD Armory button shows a low-noise ready dot only when the currently recommended next research is affordable; it never auto-opens or auto-purchases.
- Lv.3 tower defensive ward.
- Destructible castle guard towers and gates.
- Castle protection/retreat/healing logic.
- King's Hill Royal Favor.
- AI personalities: aggressive Crimson, defensive Verdant, raider Violet.
- Reinforcement waves.
- Minimap, dynamic objective/capture guidance, live siege progression, royal-finish readiness, enemy king status, battle report.
- Off-screen render culling and bounded entity/FX caps for mobile performance.
- WebAudio SFX and supported-device haptics.
- Layered battlefield terrain with roads, river crossings, forests, ridges and functional movement modifiers.
- Player army commands: Follow, Hold and Assault.
- Coherent AI kingdom frontline objectives plus local barracks reinforcement and supply healing.
- Resumable battle snapshots for mobile interruptions.
- Installable/offline-capable PWA shell with versioned service worker.
- Independent sound/haptics controls and Reduced Motion comfort mode.
- Prioritized small-screen defensive alerts for home-gate danger, castle intrusion and contested owned points.
- Off-screen defense direction guidance that supersedes lower-priority beginner guidance during critical threats.
- Desktop keyboard controls with an always-visible shortcut legend on fine-pointer devices: WASD/arrows move, Space/J attack, E build/upgrade, R rally, Q War Cry, F/Shift Royal Dash, C cycle army command, P/Escape pause/resume; T opens the Armory and 1–4 purchases research while it is open.
- Persistent in-game field manual available from intro, HUD and pause menu; desktop H toggles it. It documents the production core loop, exact tower costs, army-strengthening model, War Cry / Royal Dash behavior, command semantics, strategic-point bonuses, unit roles, terrain and siege rules.

## Target environments
- Desktop browser.
- iPhone landscape is the primary mobile target.
- iPhone portrait must show a clear rotate-device guard, not a broken game layout.
- iPad/tablet landscape must remain usable with touch controls.
- Deployment target is HTTPS static hosting such as Cloudflare Pages.

## Product principles
- King participation matters; the game must not play itself to completion routinely.
- Capturing territory must create meaningful strategic advantage.
- Siege must require army support rather than solo king rushing.
- AI kingdoms must fight each other, but early-game king deaths should not be excessively random.
- Mobile controls must remain inside safe areas and must not cause browser scrolling.
- No external runtime assets/libraries required by the game client unless deliberately introduced and verified.
