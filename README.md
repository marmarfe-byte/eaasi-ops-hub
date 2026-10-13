# EAASI Ops Hub — installable version

Summit prototype of the EAASI member platform. In this version the live data works:
latest METAR/TAF (aviationweather.gov), 3-day cloud forecast (Open-Meteo),
Meteosat cloud imagery (EUMETSAT) and rain radar (RainViewer). All free, no API keys.

## Publish on GitHub Pages (5 minutes)

1. On github.com create a new repository, e.g. `eaasi-ops`. Private is fine if your plan allows Pages on private repos; otherwise public.
2. Upload every file in this folder to the root of the repository (Add file → Upload files).
3. Settings → Pages → Source: "Deploy from a branch" → Branch `main`, folder `/ (root)` → Save.
4. After a minute the app is at `https://<your-user>.github.io/eaasi-ops/`.
5. On a phone, open that link and choose "Add to Home Screen" to install it.

## Access control

The page is marked `noindex` and `robots.txt` blocks search engines, so it only reaches people who have the link.
For real member data, put it behind Cloudflare Access (free up to 50 users): members get a one-time code by email.

## What is still a prototype

- The assistant runs in keyword-search mode here. The Claude-powered answers work inside claude.ai;
  in production they would run on a small server (e.g. a Cloudflare Worker calling the Claude API) that also handles WhatsApp.
- "Still valid" confirmations and the validation queue are stored only in the viewer's browser.

## Attribution required by the data providers

Weather data by RainViewer · Clouds © EUMETSAT · Forecast by Open-Meteo · METAR from aviationweather.gov ·
Base map © OpenStreetMap contributors © CARTO · Borders from Natural Earth.
