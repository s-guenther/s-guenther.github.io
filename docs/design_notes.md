# Design: technical notes and lessons learned

For whoever continues work on the design or technical side of sgrse.de
(the owner, another person, or an AI assistant). Status: design completed
2026-10-22 on branch `hugo`. The plan and its history are in
`design_plan.md` (local only, git-ignored because it contains strategic
notes); the concepts are explained in `docs/hugo_guide.md`.

## 1. Current state in one paragraph

Hugo extended 0.167.0 with Blowfish v3.9.0 (git submodule). German at `/`,
English at `/en/`. Teal fixed header (2.8rem) and full-width teal footer;
light grey page; one centred reading column of 36rem; Raleway for UI and
headings, Source Serif 4 for text, both self-hosted; dark mode follows the
system. Home: logo banner with fade-in, intro, three clickable tiles
linking to subheadings of the single services page, a band on the two ways
of working, a large projects button, an evidence list. Projects: list with
square thumbnails and subheadlines, detail pages with photo strip,
subheadline and lead. No resource is loaded from external servers.

## 2. Architecture decisions

| Decision | Reason |
| --- | --- |
| Hugo instead of Jekyll | Built-in multilingual support, single binary, theme as dependency instead of a fork. |
| Blowfish | Maintained, multilingual, configuration-driven, no external requests by default. |
| Theme as submodule pinned to a tag | Reproducible builds; updates are deliberate. |
| Overrides kept minimal (budget: about four partials) | The old site became unmaintainable through accumulated HTML; each override is a merge risk on theme updates. |
| All styling in one `custom.css` with numbered sections | One place to look; no Tailwind build step needed. |
| Fonts self-hosted, reduced with fontTools | GDPR (no IP transfer to Google) and page weight (167 kB total). |
| Tile data in services front matter | One source for tile texts; tiles link to anchors on the single services page. |
| Deployment unchanged in principle (build to `gh-pages`) | No GitHub settings change needed at go-live. |

## 3. Inventory of customisations

| File | Kind | What it does | Risk on theme update |
| --- | --- | --- | --- |
| `layouts/partials/header/fixed-fill.html` | replaces theme file | Wrapper with own classes `sg-header`, `sg-header-spacer`. | Low; tiny file, delegates to the theme's `header/basic.html`. |
| `layouts/partials/footer.html` | replaces theme file | Own footer: name, tagline, copyright, contact icons from `params.author.links`, legal links from footer menu; keeps the `extend-footer` hook. | Medium; theme footer features (e.g. new options) are not inherited. |
| `layouts/partials/article-meta/basic.html` | replaces theme file | On single pages: subheadline and summary as lead. Outputs nothing in lists. | Medium; the theme's meta line (dates, reading time) is gone entirely. Fine while those stay disabled. |
| `layouts/partials/header/components/translations.html` | replaces theme file | Direct link to the other language instead of a dropdown. Assumes exactly two languages. | Low. |
| `layouts/partials/extend-article-link.html` | theme hook | Subheadline under list entry titles. | Very low. |
| `layouts/shortcodes/tiles.html` | own shortcode | Reads `tiles` from `/services` front matter, images via `resources.Get` from `assets/`. | None. |
| `i18n/de.yaml`, `i18n/en.yaml` | own strings | `sg_more`; currently unused by templates since the tiles lost their buttons, kept for later use. | None. |
| `assets/css/custom.css` | stylesheet | Everything visual. Several rules target theme markup (see section 5). | Medium; selectors depend on theme class names. |

After a theme update: diff each replaced file against
`themes/blowfish/layouts/<same path>` of the old and new version, and
re-check the selectors listed in section 5.

## 4. Caveats and surprising findings

### Theme behaviour

- **`neutral` is also "white".** The theme uses `text-neutral` (330 times)
  and `bg-neutral` with `--color-neutral: 255,255,255`. Changing that
  variable for a grey page background turns button text grey. The grey
  background is therefore set on `html:not(.dark) body` in custom.css.
- **No 950 shades.** Blowfish schemes define shades 50 to 900 only; a class
  like `bg-primary-950` silently produces nothing.
- **Compiled Tailwind.** Only utility classes already used by the theme
  exist in the stylesheet. New markup in our templates must use own classes
  (prefix `sg-`) styled in custom.css.
- **`.prose` limits width.** Theme containers carry `max-w-prose`; the
  reading column is enforced by `#main-content { max-width }` plus
  resetting `max-w-prose` inside it.
- **Fixed menu heights.** The desktop nav has `h-12` (3rem) and the mobile
  row `h-14`; lowering the header needs explicit overrides of both
  (`.sg-header nav.h-12`, `.mobile-header-row`).
- **Header spacer.** The `fixed-fill` layout reserves space with a spacer
  element; our override uses `.sg-header-spacer`, whose height must equal
  the header height.
- **Logo clipping.** The logo SVG's viewBox ends exactly at the last
  letter; at some widths the "e" was clipped by a pixel or two. Fix:
  `overflow: visible` on the SVG and `flex-shrink: 0` on its container.
- **Section list cannot be switched off.** A section's `_index` page always
  shows the automatic list of its pages. This was one reason to turn the
  services section into a single page.
- **`list` shortcode unsuitable for tiles.** It forces its own heading,
  sorts by date and has no button; hence the own `tiles` shortcode.
- **Heading attributes.** `{#id}` on headings works (the theme's heading
  hook uses it as anchor). A class on a heading (`{.class}`) is dropped by
  the theme's heading render hook. On paragraphs and images, `{.class}`
  works (the image hook wraps the image in a `<figure>` carrying the class).
- **Image hook resolves `assets/`.** Markdown images are looked up first as
  page resources, then via `resources.Get` in `assets/`.
- **`article-meta/basic.html` is called with two signatures:** with a dict
  (`context`, `scope`) on single pages, and with the page itself in lists.
  The override checks `reflect.IsMap` first.
- **The `github` shortcode** fetches repository data at build time (fine)
  but loads the preview image from `opengraph.githubassets.com` in the
  visitor's browser. Use only with `showThumbnail=false`.
- **Firebase, Buy Me a Coffee** and analytics partials load external
  scripts; all disabled.
- **Simple list entries** end with an empty spacer `div.px-6` that takes
  width on phones; hidden in custom.css (`> div:last-child:empty`).

### Hugo

- **Deprecated language keys (0.158+):** `languageCode`/`languageName` are
  now `locale`/`label`.
- **Per-language permalinks** work in `languages.de.toml` under
  `[permalinks.page]` / `[permalinks.section]`.
- **Default `refLinksErrorLevel` is ERROR:** a broken `ref` stops the build
  (desired).
- **Leaf bundle images are published as files** even if only resized
  versions are used; keep source images moderate (about 1600 px).
- **New folders under `layouts/` or `i18n/`** are not always picked up by a
  running `hugo server`; restart it.

### CSS pitfalls met in this project

- **Source order inside media queries:** a mobile override placed *before*
  the base rule of equal specificity loses. Media-query blocks belong after
  the rules they modify.
- **Attribute selectors catch more than intended:** the rule hiding the
  "Start" menu entry on wide screens (`nav > a[href="/"]`) also hid the
  language switch on English pages (it links to `/`). Fixed with
  `:not(.sg-lang)`.
- **Full-bleed footer** inside the centred body: `margin-inline: calc(50% - 50vw)`
  plus `html { overflow-x: clip }` against a horizontal scrollbar.
- **Jump targets under a fixed header:** `scroll-margin-top` on `[id]` and
  `.anchor` (theme puts heading ids on a `div.anchor`).

### Fonts

- Google Fonts CSS API delivers per-subset woff2 files; the "latin" subset
  includes German umlauts and ß.
- Source Serif 4 has an optical size axis (`opsz`, 8 to 60) that doubles
  the file size; instancing to `opsz=20`, `wght=400..700` with
  `fontTools.varLib.instancer` reduced it from 122 kB to 34 kB per style
  without visible change. Re-encoding Raleway the same way made it larger,
  so Raleway is the original file.
- Raleway's default digits are old-style; `font-feature-settings: "lnum"`
  is set wherever Raleway is used.
- The `@font-face` weight ranges in custom.css must match the instanced
  ranges (Source Serif 4: 400 700).

### Deployment and environment

- Live host is `www.sgrse.de` (`static/CNAME`); `baseURL` must match.
- The workflow `.github/workflows/hugo.yml` runs only on pushes to
  `master`; it pins Hugo 0.167.0 and checks out submodules. Keep the Hugo
  version within the theme's range.
- `peaceiris/actions-gh-pages` adds `.nojekyll`, so GitHub Pages does not
  run Jekyll on the built files.
- The old Jekyll site remains on `develop`/`master` until go-live.

## 5. CSS selectors that depend on theme markup

Re-check these after a theme update (all in `assets/css/custom.css`):

| Selector | Theme element |
| --- | --- |
| `.logo svg` | Inline SVG logo in `header/basic.html`. |
| `.sg-header .main-menu > div:first-child` | Logo container in `header/basic.html`. |
| `.sg-header nav.h-12`, `.mobile-header-row` | Menu bar heights. |
| `.sg-header .md\:flex nav > a[href=...]` | Desktop menu links (hiding "Start"). |
| `.sg-header .menuhide`, `#mobile-menu-dialog` | Dropdown panels and mobile menu. |
| `#main-content`, `.max-w-prose`, `.prose` | Page column. |
| `#single_header h1` | Title on single pages. |
| `#main-content article > .overflow-hidden:first-child` | Photo strip (`hero/basic.html`). |
| `.article-link--simple`, `.thumbnail`, `.article-link__summary` | List entries (`article-link/simple.html`). |
| `.anchor` | Heading anchors (`_markup/render-heading.html`). |

## 6. Verification workflow used

- **Build check:** `hugo --gc --minify -d <tmp dir>`; expect no WARN/ERROR.
- **No external requests:** in the built HTML, no `src`/`srcset` and no
  stylesheet/preload/icon `href` pointing to another host; no external
  `url()` in CSS. (Plain outbound links and `<link rel="me">` are fine.)
- **Clean clone:** `git clone --branch hugo --recurse-submodules` into a
  temporary folder and build there.
- **Screenshots (headless):** snap Firefox can only write inside
  `~/snap/firefox/common/`:

  ```bash
  D=~/snap/firefox/common/claude-shots
  firefox --headless --profile $D/profile --no-remote \
    --window-size=1280,1200 --screenshot $D/x.png http://127.0.0.1:4000/
  ```

  Separate profiles for light and dark: a profile's `user.js` with
  `user_pref("ui.systemUsesDarkTheme", 1);`. Set
  `user_pref("ui.prefersReducedMotion", 1);` so the banner fade-in does not
  show half-transparent. Limits: lazily loaded images may be missing (take
  the screenshot again or ignore); jump links (`#anchor`) are not scrolled
  to; the page is captured from the top only up to the window height; the
  mobile menu cannot be opened, so it was checked by temporarily adding
  `#mobile-menu-dialog{visibility:visible!important;opacity:1!important}`
  to custom.css and removing it afterwards.
- **Widths checked:** 1280, 1100, 1024, 900, 820, 768, 700, 600, 400 px.

## 7. Working environment notes

- The owner views the preview via an SSH tunnel to port 4000 from Windows.
- A server started by an AI assistant session runs as a background task of
  that session and stops when the session ends; the owner then sees
  "connection refused". Starting it in the owner's own terminal (or `tmux`)
  avoids this.
- `pkill -f "hugo server"` inside a shell whose own command line contains
  that string kills the shell itself; start/stop the server in separate
  commands.
- `~/.local/bin` is only on the PATH of shells started after login.

## 8. Open design options (not required)

- Dropdown menus for Leistungen/Projekte (menu entries with `parent`).
- Previous/next links on project pages (theme option `showPagination`; it
  would also chain unrelated top-level pages, hence off).
- Replace stock photos with own material (figures from papers, renderings).
- Fade-in of the home banner: kept; remove the `animation` line in
  custom.css section 6 to drop it.
- Redirects from old English URLs (`/about/`, `/projects/...`) via
  `aliases` in front matter.
