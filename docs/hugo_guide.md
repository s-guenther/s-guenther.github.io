# Working with this site: Hugo and Blowfish explained

A guide for maintaining sgrse.de without prior web development experience.
It explains the concepts behind Hugo and the Blowfish theme, how this
project is organised, and how to do the usual tasks. The README is the short
reference; this document is the explanation.

Contents:

1. What Hugo does
2. Core Hugo concepts
3. The Blowfish theme
4. How this project is organised
5. Everyday tasks
6. Markdown as used here
7. Styling
8. Building, previewing, deploying
9. Troubleshooting
10. Further reading

---

## 1. What Hugo does

Hugo is a *static site generator*. It reads Markdown files (the text),
configuration files (settings) and templates (the page frame), and writes
plain HTML, CSS and image files into a folder (`public/`). These files are
the website. There is no database, no server program and no login: a web
server only hands out finished files. This is why hosting on GitHub Pages is
free and simple, and why the site has nothing to attack or update on the
server side.

Two ways to run Hugo:

- `hugo server`: builds the site in memory, serves it on a local port and
  rebuilds on every saved change (the browser reloads automatically). For
  writing and checking.
- `hugo`: builds once into `public/`. This is what the deployment does.

Hugo is a single program file (`~/.local/bin/hugo`). It needs no other
installation. The "extended" edition is required by the theme.

## 2. Core Hugo concepts

### 2.1 Content and front matter

Every page is a Markdown file under `content/`. It starts with a *front
matter* block between two `---` lines, written in YAML:

```markdown
---
title: "Speicherauslegung für Windparks"
slug: "windpark"
summary: "Werkzeug, das für einen Windpark prüft, ob sich ein Speicher lohnt."
weight: 30
---

Here starts the text in Markdown.
```

Front matter holds data about the page (title, order, short summary, URL
part); the text below it is the visible content. Templates decide which
front matter fields appear where. Lines starting with `#` inside front
matter are comments.

### 2.2 Sections, pages and bundles

- A **section** is a folder directly under `content/` that contains several
  pages, e.g. `content/projects/`. Its overview page is `_index.md` (with an
  underscore). Hugo automatically lists the section's pages on it.
- A **page bundle** is a folder for one page together with its files, e.g.
  `content/projects/flywheel/` with `index.de.md`, `index.en.md` and
  `featured.jpg`. The page can use the images in its folder directly. Note
  the difference: `index.md` = one page with files (leaf bundle),
  `_index.md` = section overview (branch bundle).
- A **single file** such as `content/about.de.md` is a page without own
  files.

The home page is `content/_index.*.md`.

### 2.3 URLs

By default the URL follows the file path: `content/about.en.md` becomes
`/en/about/`. Two ways to change it:

- `slug:` in front matter replaces the last URL part. German pages use this
  (`slug: "ueber-mich"` gives `/ueber-mich/`).
- `permalinks` in the configuration change URL patterns for a whole
  section. Here: German projects live under `/projekte/` instead of
  `/projects/` (set in `config/_default/languages.de.toml`).

Never type URLs by hand in links; use `{{< ref "about" >}}` (see 6.2). Hugo
then finds the right URL in the right language, and a broken link stops the
build with an error instead of silently producing a dead link.

### 2.4 Multilingual sites

Hugo supports several languages natively:

- Languages are defined in `config/_default/languages.de.toml` and
  `languages.en.toml` (name, order, site title, author data).
- `defaultContentLanguage = "de"` and
  `defaultContentLanguageInSubdir = false` in `hugo.toml` put German at `/`
  and English at `/en/`.
- **Translation by file name:** `about.de.md` and `about.en.md` in the same
  folder are recognised as the same page in two languages. Hugo links them,
  which is what the EN/DE switch in the header uses. A page that exists in
  one language only (Impressum) simply has no switch.
- **Menus per language:** `menus.de.toml` and `menus.en.toml`.
- **Interface words** (e.g. "Mehr", "Weiterlesen" in templates) come from
  translation files in `i18n/de.yaml` and `i18n/en.yaml`. The theme brings
  its own; this site adds a few in its own `i18n/` folder.

### 2.5 Templates, partials and the lookup order

Templates are HTML files with placeholders (Go template language, e.g.
`{{ .Title }}`). They define the page frame. You will rarely touch them, but
it helps to know how Hugo finds them:

- **Layouts** describe whole page types: `single.html` for a normal page,
  `list.html` for a section overview, plus a base frame (`baseof.html`).
- **Partials** are reusable pieces, e.g. the header or the footer
  (`layouts/partials/...`).
- **Lookup order:** Hugo first looks in the project's own `layouts/` folder,
  then in the theme's (`themes/blowfish/layouts/`). A file in the project
  with the same path as a theme file **replaces** the theme file. This is
  how this site changes the theme without editing it (see 4.3).

### 2.6 Shortcodes

A shortcode is a small template you can call from Markdown, written in
double curly braces with angle brackets:

```markdown
{{< tiles >}}
{{< icon "email" >}}
{{< ref "projects/wind-farm" >}}
```

`ref` is built into Hugo; `icon` comes from the theme; `tiles` is defined in
this project (`layouts/shortcodes/tiles.html`). Shortcodes keep HTML out of
the Markdown files.

### 2.7 Render hooks

Render hooks are templates that change how Markdown elements become HTML,
for example images or links. The theme uses one for images: it looks for the
image first in the page's own folder, then in `assets/`, and scales it
automatically. That is why `![Alt text](img/portrait.jpg)` works although
the file is in `assets/img/`.

### 2.8 assets/ versus static/

- `assets/`: files Hugo *processes* (scaling and cropping images, bundling
  CSS). Referenced in Markdown or templates by path, e.g. `img/portrait.jpg`.
- `static/`: files copied *unchanged* to the website root, e.g. fonts,
  favicons, `CNAME`. `static/fonts/x.woff2` becomes `/fonts/x.woff2`.

### 2.9 Configuration

All settings are in `config/_default/`:

| File | Content |
| --- | --- |
| `hugo.toml` | Core settings: address of the site, theme, default language, disabled features. |
| `params.toml` | Theme options (Blowfish): layouts, colours, what to show on pages. |
| `languages.*.toml` | Per language: name, site title, author, contact links, German URL patterns. |
| `menus.*.toml` | Header and footer menus per language. |
| `markup.toml` | How Markdown is converted; required settings for the theme. |

TOML syntax: `key = "value"`, sections in `[brackets]`, lists of entries
with `[[double brackets]]`. Changes are picked up by the running server
automatically.

## 3. The Blowfish theme

### 3.1 What a theme provides

A theme is a complete set of templates, styles, icons, shortcodes and
translations. Blowfish (https://blowfish.page) was chosen because it
supports multiple languages well, is actively maintained, keeps almost all
configuration in TOML files and front matter, and loads nothing from
external servers by default.

### 3.2 How the theme is included

The theme lives in `themes/blowfish/` as a **git submodule**: a pointer to a
fixed version (tag `v3.9.0`) of the theme's own repository. Consequences:

- Never edit files in `themes/blowfish/`; changes would be lost on update
  and are not part of this repository.
- After cloning the project: `git submodule update --init` downloads the
  theme.
- The theme requires a Hugo version within a range given in
  `themes/blowfish/config.toml` (currently 0.164.0 to 0.167.0). The same
  version is pinned in the deployment workflow.

### 3.3 Theme options

Most of the appearance is controlled in `config/_default/params.toml`:
colour scheme, home page layout (`page` here), header layout (`fixed-fill`
here), which details appear on pages (dates, reading time, etc., all
switched off here), dark mode behaviour. Each option is documented in the
theme's own `config/_default/params.toml` and at
https://blowfish.page/docs/configuration/.

### 3.4 Colour schemes and Tailwind

Blowfish uses Tailwind CSS, a system of predefined style classes. The theme
ships a **precompiled** stylesheet. Consequence: in our own templates or
Markdown we cannot simply use arbitrary Tailwind class names, only those the
theme already uses. For our own styling we write normal CSS in
`assets/css/custom.css` (loaded automatically by the theme).

Colours come from a *scheme*: a file defining three colour scales (neutral,
primary, secondary) with ten shades each. Ours is
`assets/css/schemes/sgrse.css`, generated from the logo colours by
`tools/color_scale.py`.

### 3.5 Extension points

The theme offers several ways to customise without replacing files:

- **Hooks:** partials with special names that the theme includes if they
  exist, e.g. `extend-head.html`, `extend-footer.html`,
  `extend-article-link.html` (used here for the project subheadlines).
- **custom.css:** automatically loaded after the theme's styles.
- **Own shortcodes and i18n strings** in the project folders.
- **Overrides** (replacing a theme file, see 2.5) as the last resort.

## 4. How this project is organised

### 4.1 Folder structure

```
s-guenther.github.io/
├── content/                 the text (Markdown), see 4.2
├── config/_default/         settings (TOML)
├── assets/
│   ├── css/custom.css       all site styling on top of the theme
│   ├── css/schemes/sgrse.css   colour palette
│   └── img/                 logos, portrait, contact and services images
├── layouts/                 replaced theme files, hook, shortcode (4.3)
├── i18n/                    own interface words (de/en)
├── static/                  fonts, favicons, CNAME (copied as is)
├── themes/blowfish/         the theme (submodule, do not edit)
├── tools/color_scale.py     generator for the colour palette
├── docs/                    this guide and the technical design notes
├── .github/workflows/hugo.yml   deployment
└── README.md                short reference
```

Generated or private, not in git: `public/` (build output),
`resources/_gen/` (Hugo's image cache), `__personal/`, `CLAUDE.md`.

### 4.2 Content files

```
content/
├── _index.de.md / .en.md          home page
├── services.de.md / .en.md        services (one page; defines the home tiles)
├── about.de.md / .en.md           about
├── contact.de.md / .en.md         contact
├── impressum.de.md                German only
├── datenschutz.de.md              German only
└── projects/
    ├── _index.de.md / .en.md      projects overview (list is automatic)
    └── <project>/                 one folder per project
        ├── index.de.md
        ├── index.en.md
        └── featured.jpg           thumbnail and photo strip
```

Front matter fields used on this site:

| Field | Where | Effect |
| --- | --- | --- |
| `title` | all | Heading and browser tab. |
| `slug` | German pages | German URL part. |
| `description` | all | Text for search engines and link previews (not visible). |
| `subheadline` | projects | Small caps line under the title, in the list and on the page. |
| `summary` | projects | Text in the project list and lead paragraph on the page. |
| `weight` | projects | Order in the list (lower first). |
| `tiles` | services | Data for the three home page tiles. |

### 4.3 What is customised and how

Changes to the theme, all documented in the README table "Theme overrides":

- **Header** (teal bar): replaced `layouts/partials/header/fixed-fill.html`.
- **Footer** (teal bar with icons): replaced `layouts/partials/footer.html`.
- **Subheadline and lead on pages:** replaced
  `layouts/partials/article-meta/basic.html`.
- **Language switch** (one click): replaced
  `layouts/partials/header/components/translations.html`.
- **Subheadline in lists:** theme hook `layouts/partials/extend-article-link.html`.
- **Tiles:** own shortcode `layouts/shortcodes/tiles.html`.
- **Everything visual** (fonts, colours, sizes, column width, tiles, list
  layout): `assets/css/custom.css`, organised in numbered sections.

Each of these files starts with a comment explaining why it exists.

## 5. Everyday tasks

Always: start the preview (section 8), edit, check in the browser, commit.

### 5.1 Change text

Open the Markdown file, edit, save. Change both language versions. The
preview reloads automatically.

### 5.2 Add a project

1. Copy a project folder, e.g. `content/projects/wind-farm/` to
   `content/projects/new-name/`.
2. Edit `index.de.md` and `index.en.md`: `title`, `slug` (German only),
   `subheadline`, `summary`, `weight` (position in the list), text.
3. Replace `featured.jpg` with a photo (any size and format ratio; Hugo
   crops it to a square for the list and a strip for the page).

### 5.3 Change the service tiles on the home page

Edit the `tiles` list at the top of `content/services.de.md` and
`services.en.md`: title, text, image (path inside `assets/`), anchor. The
anchor is the jump target on the services page and must match a heading
there, e.g. `## Forschungssoftware {#research-software}`. Anchors are the
same in both languages.

### 5.4 Add or replace an image

- Image belonging to one project: into the project folder.
- Image used elsewhere: into `assets/img/`, referenced as `img/name.jpg`.
- Large photos are fine; Hugo produces scaled versions. For the repository
  size, photos above about 1600 px width are not useful.

### 5.5 Change the menu

`config/_default/menus.de.toml` and `menus.en.toml`. Each entry: `name`,
`pageRef` (the page, as for `ref`), `weight` (order). The first entry
("Start"/"Home") appears only in the burger menu on small screens.

### 5.6 Change contact data

Footer icons and their links: `[params.author] links` in
`languages.de.toml` and `languages.en.toml`. Contact page text:
`content/contact.*.md`. Impressum: `content/impressum.de.md`.

### 5.7 Change colours

Edit or regenerate `assets/css/schemes/sgrse.css`:

```bash
python3 tools/color_scale.py primary "#00897c"
```

prints a scale to paste into the file. Primary (teal) is used for links,
buttons, header and footer; secondary (slate blue) for headings.

### 5.8 Find open placeholders

```bash
grep -rn TODO content
```

## 6. Markdown as used here

### 6.1 Basics

```markdown
## Heading level 2          (### for level 3)
**bold**, *italic*
- list item
1. numbered item
[link text](https://example.org)
![image description](img/portrait.jpg)
```

A line ending with a backslash `\` forces a line break within a paragraph.

### 6.2 Links between pages

```markdown
[Über mich]({{< ref "about" >}})
[Windpark]({{< ref "projects/wind-farm" >}})
[Zusammenarbeit]({{< ref "services" >}}#zusammenarbeit)
```

The path is the file path inside `content/` without language and extension.
Hugo inserts the correct URL for the current language.

### 6.3 Block attributes

A line `{.classname}` directly below a paragraph or image assigns a style
class to it. Used on this site:

| Attribute | Effect |
| --- | --- |
| `{.sg-page-banner}` | Image as wide banner (services, contact). |
| `{.sg-portrait}` | Image floats right of the text (about). |
| `{.sg-banner}` | Logo banner with fade-in (home). |
| `{.sg-band}` | Highlighted box with teal edge (home). |
| `{.sg-more}` | Paragraph with one link shown as a small button. |
| `{.sg-cta}` | Paragraph with one link shown as a large full-width button. |
| `{.sg-contact-lines}` | Contact lines with icons (contact). |

Headings can get a fixed jump target: `## Forschungssoftware {#research-software}`.

### 6.4 Shortcodes used

| Shortcode | Effect |
| --- | --- |
| `{{< ref "path" >}}` | URL of another page (Hugo built-in). |
| `{{< icon "email" >}}` | Inline icon; names are the files in `themes/blowfish/assets/icons/`. |
| `{{< tiles >}}` | The three service tiles (home). |

The theme offers about 40 more (buttons, alerts, galleries, timelines):
https://blowfish.page/docs/shortcodes/.

## 7. Styling

- Fonts: Raleway (headings, navigation, buttons; the logo's typeface) and
  Source Serif 4 (running text), served from `static/fonts/`. No request
  goes to Google.
- Light mode: light grey background, teal bars, slate blue headings. Dark
  mode follows the visitor's system setting; the switch in the header
  overrides it.
- One centred reading column (36rem wide); header and footer span the full
  width.
- All of it is in `assets/css/custom.css`. Each section of that file starts
  with a comment; values such as column width or header height are easy to
  find there.

## 8. Building, previewing, deploying

### 8.1 Preview

In an SSH session on the server:

```bash
cd ~/s-guenther.github.io
~/.local/bin/hugo server --bind 127.0.0.1 --port 4000 --liveReloadPort 4000
```

On the Windows client, with the tunnel
`ssh -L 4000:127.0.0.1:4000 x870e`, open http://localhost:4000/. The server
runs until Ctrl+C or until the terminal closes (`tmux` keeps it running).
After adding new folders under `layouts/` or `i18n/`, restart it.

### 8.2 Deploy

The live site is built by GitHub, not on this computer:

1. Work happens on a branch (currently `hugo`).
2. A push to `master` starts `.github/workflows/hugo.yml` on GitHub.
3. That workflow builds the site with the pinned Hugo version and pushes the
   result to the `gh-pages` branch.
4. GitHub Pages publishes `gh-pages` at www.sgrse.de.

Pushing other branches publishes nothing.

### 8.3 Updating the theme

```bash
cd themes/blowfish && git fetch --tags && git checkout v3.10.0 && cd ../..
```

(version as needed). Then: check the Hugo version range in
`themes/blowfish/config.toml`, compare the four replaced theme files with
their originals, build, check the preview, commit.

## 9. Troubleshooting

| Symptom | Cause and fix |
| --- | --- |
| `hugo: command not found` | Call `~/.local/bin/hugo`, or log in again (the folder is added to the search path at login). |
| Browser: connection refused or reset | The preview server is not running; start it (8.1). |
| Build error "REF_NOT_FOUND" | A `ref` points to a page that does not exist; check the path. |
| Change not visible | Hard reload in the browser (Ctrl+F5); for new layout files restart the server. |
| Page appears in one language only | The other language file is missing or named differently. |
| Image does not appear | Path wrong, or the file is in `static/` instead of `assets/` or the page folder. |
| Styling looks broken after a theme update | Compare the replaced theme files (README) with the new theme versions. |

## 10. Further reading

- Hugo documentation: https://gohugo.io/documentation/ (especially
  "Content management", "Multilingual", "Templates")
- Blowfish documentation: https://blowfish.page/docs/
- Markdown in Hugo (Goldmark): https://gohugo.io/content-management/formats/
- Technical notes on this site's design and its pitfalls:
  `docs/design_notes.md`
