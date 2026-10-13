"""Builds ../index.html (the installable PWA) from the template and the JSON data.
Run from anywhere:  python src/build.py
Edit the data in src/data/*.json and the app in src/app.template.html, then rebuild."""
import json, base64, pathlib
SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parent
tpl = (SRC / "app.template.html").read_text(encoding="utf-8")
data = {k: json.loads((SRC / "data" / f"{k}.json").read_text(encoding="utf-8"))
        for k in ["permits", "radar", "airports", "mro", "insurance", "assets", "europe"]}
logo = "data:image/png;base64," + base64.b64encode((SRC / "eaasi_logo_dark.png").read_bytes()).decode()
body = (tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
           .replace("__LOGO__", logo)
           .replace("/*__LEAFLET_CSS__*/", (SRC / "leaflet.css").read_text(encoding="utf-8")))
head = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#1A2340">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png">
<link rel="apple-touch-icon" href="icon-192.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
tail = """
<script>if("serviceWorker" in navigator){addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}));}</script>
</body>
</html>
"""
(ROOT / "index.html").write_text(head + body + tail, encoding="utf-8")
print("Built", ROOT / "index.html")
