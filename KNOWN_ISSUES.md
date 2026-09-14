# KNOWN ISSUES

## Open
- Live iOS Safari PWA installation/service-worker behavior still requires validation on the deployed HTTPS build; this environment validates the PWA asset contract and Chromium runtime but cannot drive real Safari.
- Test environment policy blocks browser navigation to localhost/file URLs, so browser regression uses Playwright `set_content` plus explicit release-asset checks. This still executes the real application JavaScript/CSS in Chromium, but does not exercise an actual HTTP navigation in this environment.
- Direct ChatGPT iPhone attachment preview is not a supported runtime; the game must be served via HTTPS for reliable iPhone execution.
- Battlefield art is now substantially richer, but it is still code-drawn vector styling rather than a bespoke illustrated asset pack with dedicated animation frames.
- AI kingdoms cannot permanently eliminate one another; this is deliberate to preserve the player-king finishing objective, but future design may add a richer incapacitation/capture state.

## Closed historical issues
- Armory cards now preview exact next-level effects before purchase (fixed by 0.93.3).
- Frequent unattended auto-victory fixed by player-king-only royal finishing rule in 0.41.0.
- Monolithic-source maintenance risk reduced by generated single-file architecture in 0.40.2.
- Missing repository manifest fixed in 0.40.1.
- AI early king self-elimination reduced.
- Late-game stalemate reduced through escalation logic.
- Unit/projectile runaway constrained.
- Mobile attack, joystick, rotation guard, pause behavior and compact HUD overlap resilience hardened.
