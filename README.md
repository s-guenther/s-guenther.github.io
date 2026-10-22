# sgrse website

Source of [sgrse.de](https://sgrse.de), built with [Hugo](https://gohugo.io)
and the [Blowfish](https://blowfish.page) theme. German is the main language
(`/`), English is at `/en/`.

## Where things are

| Path | Content |
| --- | --- |
| `content/` | All pages as Markdown. Translations sit side by side: `about.de.md` and `about.en.md`. |
| `content/_index.*.md` | Home page. |
| `content/services.*.md` | The services page. The home page tiles are defined in its front matter (`tiles`); banner and tile images are in `assets/img/services/`. |
| `content/projects/<name>/` | One folder per project: `index.de.md`, `index.en.md`, `featured.jpg`. |
| `config/_default/` | Site settings (`hugo.toml`), theme options (`params.toml`), per-language title, author and contact links (`languages.*.toml`), menus (`menus.*.toml`). |
| `assets/img/` | Logos, portrait, contact photo, services images. |
| `assets/css/schemes/sgrse.css` | Colour palette from the logo (generated with `tools/color_scale.py`). |
| `assets/css/custom.css` | All site styling on top of the theme, in numbered sections. |
| `layouts/` | The few theme files replaced for this site, see below. |
| `i18n/` | Site-specific interface words (e.g. "Mehr"/"More"). |
| `static/` | Files copied as is: fonts, favicons, `CNAME`. |
| `themes/blowfish/` | The theme as a git submodule. Do not edit; override instead. |

## Writing content

Each page starts with a front matter block between `---` lines:

```yaml
---
title: "Speicherauslegung für Windparks"
slug: "windpark"        # German URL; English pages use the folder name
subheadline: "Industrieprojekt parallel zur Promotion"   # small caps line
summary: "Text for the list entry or tile, and lead on the page itself."
weight: 30              # order in lists and tiles (lower first)
---
```

- Link to other pages with `{{< ref "about" >}}` or
  `{{< ref "projects/wind-farm" >}}`; Hugo resolves it to the page in the same
  language.
- **New project:** copy an existing project folder, adapt both
  `index.*.md` files, replace `featured.jpg` (any size; Hugo crops it for
  the thumbnail and the photo strip).
- **Service tiles:** edit the `tiles` list in `content/services.*.md`
  (title, text, image path in `assets/`, anchor). Each tile links to the subheading with that
  anchor, written in Markdown as `## Forschungssoftware {#research-software}`.
  Anchors are the same in both languages.
- **Banner photo inside a page:** put the image line in Markdown and
  `{.sg-page-banner}` on the line directly below it. `{.sg-portrait}` floats
  an image to the right (About page). `{.sg-band}`, `{.sg-more}` and
  `{.sg-cta}` below a paragraph give the highlighted band, a small button
  and a large full-width button (home page).
- **Tiles:** `{{< tiles >}}` shows the three service tiles (home page).
- **Menu:** `config/_default/menus.*.toml`. The first entry ("Start" /
  "Home") is shown only in the burger menu on narrow screens.
- Placeholders that still need facts are marked `**[TODO: ...]**`; list them
  with `grep -rn TODO content`.

## Theme overrides

Hugo uses a file in `layouts/` instead of the theme file with the same path.
These are all replacements and additions; each file explains itself in a
comment at the top.

| File | Kind | Reason |
| --- | --- | --- |
| `layouts/partials/header/fixed-fill.html` | replaces theme file | Teal header bar across the full width. |
| `layouts/partials/footer.html` | replaces theme file | Teal footer with tagline, contact icons and legal links. |
| `layouts/partials/article-meta/basic.html` | replaces theme file | Subheadline and lead under the title of detail pages. |
| `layouts/partials/header/components/translations.html` | replaces theme file | Language switch toggles directly instead of opening a dropdown. |
| `layouts/partials/extend-article-link.html` | theme hook | Subheadline in list entries. |
| `layouts/shortcodes/tiles.html` | new shortcode | Clickable service tiles (photo, title, text), data from the services page. |

After a theme update, compare the replaced files with their originals in
`themes/blowfish/layouts/` (same path) for relevant changes.

## Fonts

Raleway (typeface of the logo; headings, navigation, buttons) and Source
Serif 4 (running text), both under the SIL Open Font License
(`static/fonts/OFL-*.txt`). They are served from this site, not from Google,
so no visitor data goes to Google. Files: the "latin" subset from Google
Fonts; Source Serif 4 was reduced with fontTools to optical size 20 and
weights 400 to 700 (from about 120 kB to 34 kB per style):

```python
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
font = instancer.instantiateVariableFont(
    TTFont("sourceserif4-latin.woff2"), {"opsz": 20, "wght": (400, 700)})
font.flavor = "woff2"
font.save("sourceserif4-latin.woff2")
```

## Local preview

Requires Hugo **extended**, version as in `.github/workflows/hugo.yml`
(currently 0.167.0), e.g. installed to `~/.local/bin`. If the shell does not
find `hugo`, call it as `~/.local/bin/hugo` or log in again (`~/.profile`
adds `~/.local/bin` to the search path at login).

```bash
git submodule update --init      # once, after cloning
hugo server --bind 127.0.0.1 --port 4000 --liveReloadPort 4000
```

Then open http://localhost:4000/. Changes to content and styles reload
automatically; after adding new folders under `layouts/` or `i18n/`, restart
the server.

## Deployment

A push to `master` runs `.github/workflows/hugo.yml`: it builds the site and
pushes the result to the `gh-pages` branch, which GitHub Pages serves.
Other branches are not deployed.

## Updating the theme

```bash
cd themes/blowfish && git fetch --tags && git checkout <new-tag> && cd ../..
```

Check the supported Hugo range in `themes/blowfish/config.toml`, adjust the
Hugo version in the workflow if needed, compare the overrides (see above),
build locally, then commit.
