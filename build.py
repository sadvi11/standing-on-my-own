#!/usr/bin/env python3
"""Build the site from posts/*.md.

    pip install markdown
    python3 build.py

Or add a file to posts/ on GitHub and the Action does it.

Two kinds of writing, set by `kind:` in the front matter:

    note   - short, daily, thinking out loud
    essay  - longer, worked out, the ones worth sending someone

Both are dated and both appear on the front page. The split exists so that
writing daily does not mean every piece has to be finished.
"""
from __future__ import annotations

import pathlib
import re
import sys
from datetime import date as _date

try:
    import markdown
except ImportError:
    sys.exit("pip install markdown")

HERE = pathlib.Path(__file__).resolve().parent
POSTS = HERE / "posts"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Sadhvi Sharma</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="wrap">

<header class="site">
  <a class="name" href="/standing-on-my-own/">Standing on my own</a>
  <nav>
    <a href="/standing-on-my-own/">Writing</a>
    <a href="/standing-on-my-own/speaking.html">Speaking</a>
    <a href="/standing-on-my-own/about.html">About</a>
  </nav>
</header>

<h1>{title}</h1>
<p class="lede">{lede}</p>
<p class="date">{kind} · {date}</p>

{body}

<footer>
  <p><a href="/standing-on-my-own/">← everything else</a></p>
</footer>

</div>
</body>
</html>
"""


def parse(path: pathlib.Path) -> dict:
    text = path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        sys.exit(f"{path.name}: missing the --- front matter block")

    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            sys.exit(f"{path.name}: front matter line is not key: value -> {line!r}")
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()

    for req in ("title", "lede", "date"):
        if not meta.get(req):
            sys.exit(f"{path.name}: front matter needs a non-empty '{req}'")
    try:
        _date.fromisoformat(meta["date"])
    except ValueError:
        sys.exit(f"{path.name}: date must be YYYY-MM-DD, got {meta['date']!r}")

    meta.setdefault("kind", "note")
    if meta["kind"] not in ("note", "essay"):
        sys.exit(f"{path.name}: kind must be 'note' or 'essay'")
    meta["body_md"] = m.group(2)
    meta["slug"] = path.stem
    meta.setdefault("description", meta["lede"])
    return meta


def pretty(iso: str) -> str:
    d = _date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B %Y')}"


def main() -> int:
    paths = sorted(p for p in POSTS.glob("*.md") if p.stem != "TEMPLATE")
    if not paths:
        sys.exit("no posts found in posts/")

    posts = [parse(p) for p in paths]
    posts.sort(key=lambda p: p["date"], reverse=True)   # newest first

    for p in posts:
        body = markdown.markdown(
            p["body_md"], extensions=["extra", "sane_lists", "smarty"])
        (HERE / f"{p['slug']}.html").write_text(PAGE.format(
            title=p["title"], description=p["description"].replace('"', "&quot;"),
            lede=p["lede"], kind=p["kind"], date=pretty(p["date"]), body=body))
        print(f"  {p['date']}  {p['kind']:6} {p['slug']}.html")

    entries = "\n".join(
        f'\n  <a class="entry" href="{p["slug"]}.html">\n'
        f'    <span class="d">{pretty(p["date"])} · {p["kind"]}</span>\n'
        f'    <h3>{p["title"]}</h3>\n'
        f'    <p>{p["lede"]}</p>\n'
        f'  </a>' for p in posts)

    idx = (HERE / "index.html").read_text()
    if "<!-- POSTS -->" not in idx:
        sys.exit("index.html is missing the <!-- POSTS --> markers")
    (HERE / "index.html").write_text(re.sub(
        r"(<!-- POSTS -->).*?(<!-- /POSTS -->)",
        lambda m: f"{m.group(1)}\n{entries}\n  {m.group(2)}", idx, flags=re.S))
    print(f"\n  {len(posts)} pieces")
    return 0


if __name__ == "__main__":
    sys.exit(main())
