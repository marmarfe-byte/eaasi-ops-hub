# Source of the EAASI Ops Hub

- `app.template.html` — the app (layout, styles, logic). Placeholders are filled by the build.
- `data/*.json` — the content: permits, radar, airports, mro, insurance, assets, europe (base map).
- `build.py` — run `python src/build.py` to regenerate `../index.html`.

Only the files in the parent folder are published. This `src` folder does not need to go online.
