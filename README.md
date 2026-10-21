# sgrse website

Source of [sgrse.de](https://sgrse.de), built with [Hugo](https://gohugo.io)
and the [Blowfish](https://blowfish.page) theme. German is the main language
(`/`), English is at `/en/`.

## Where things are

| Path | Content |
| --- | --- |
| `content/` | All pages as Markdown. Translations sit side by side: `about.de.md` and `about.en.md`. |
| `content/projects/<name>/` | One folder per project: `index.de.md`, `index.en.md`, optional `featured.jpg`. |
| `config/_default/` | Site settings (`hugo.toml`), theme options (`params.toml`), per-language title, author and links (`languages.*.toml`), menus (`menus.*.toml`). |
| `assets/img/` | Logo and portrait. |
| `assets/css/schemes/sgrse.css` | Colour palette from the logo (generated with `tools/color_scale.py`). |
| `assets/css/custom.css` | The few style adjustments on top of the theme. |
| `static/` | Files copied as is: favicons, `CNAME`. |
| `themes/blowfish/` | The theme as a git submodule. Do not edit; override instead. |

## Writing content

Each page starts with a front matter block between `---` lines:

```yaml
---
title: "Leistungen"
slug: "leistungen"      # German URL; English pages use the file name
description: "Short text for search engines and link previews."
---
```

Link to other pages with `{{< ref "about" >}}`; Hugo resolves it to the
page in the same language. Projects are ordered by `weight` (lower first) and
listed with their `summary`.

Placeholders that still need facts are marked `**[TODO: ...]**`; list them
with `grep -rn TODO content`.

## Local preview

Requires Hugo **extended**, version as in `.github/workflows/hugo.yml`
(currently 0.167.0), e.g. installed to `~/.local/bin`.

```bash
git submodule update --init      # once, after cloning
hugo server --bind 127.0.0.1 --port 4000 --liveReloadPort 4000
```

Then open http://localhost:4000/. Changes to content reload automatically.

## Deployment

A push to `master` runs `.github/workflows/hugo.yml`: it builds the site and
pushes the result to the `gh-pages` branch, which GitHub Pages serves.
Other branches are not deployed.

## Updating the theme

```bash
cd themes/blowfish && git fetch --tags && git checkout <new-tag> && cd ../..
```

Check the supported Hugo range in `themes/blowfish/config.toml`, adjust the
Hugo version in the workflow if needed, build locally, then commit.
