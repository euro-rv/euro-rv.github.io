# Euro-RV Workshop @ MICRO 2026

**Euro-RV: European Workshop on Hardware-Software Co-Design for Future RISC-V Architectures**

Static site for the Euro-RV workshop, co-located with [MICRO 2026](https://microarch.org/micro59/) in Athens, Greece. Organized by [BSC](https://www.bsc.es/) and [IMEC](https://www.imec-int.com/).

Layout adapted from the [Arch4Health](https://github.com/nikamgh/arch4health) workshop site ([live demo](https://events.safari.ethz.ch/micro25-arch4health/)).

## Local preview

### Quick preview (no Ruby/Jekyll)
```bash
./serve
```

Opens [http://127.0.0.1:4000](http://127.0.0.1:4000). Uses a tiny Python server that renders `index.md` on the fly. On first run it may install the `markdown` pip package.

Options:

```bash
./serve --port 8080      # custom port
./serve --no-open        # don't open a browser tab
```

### Full Jekyll preview (matches GitHub Pages exactly)

```bash
bundle install
bundle exec jekyll serve
```

Open [http://localhost:4000](http://localhost:4000).

## Deploy on GitHub Pages

1. Push this repo to GitHub as `euro-rv/euro-rv.github.io` (or your org/user Pages repo).
2. In **Settings → Pages**, set source to **Deploy from branch** → `main` → `/ (root)`.
3. GitHub builds Jekyll automatically using `_config.yaml` and the `github-pages` gem.

## Structure

Same sections as the Arch4Health template:

- Workshop description with anchor navigation
- Call for presentations
- Key dates
- Organizer bios (photo + text layout)
- Agenda table with coffee-break styling
- Optional livestream block (commented out in the scaffold)

## Credits

Layout and styling adapted from [nikamgh/arch4health](https://github.com/nikamgh/arch4health) (Jekyll + `pages-themes/primer`).
