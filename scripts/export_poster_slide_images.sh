#!/usr/bin/env bash
# Export first slide of each poster PPTX from the workshop Drive folder to WebP for the site carousel.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$REPO_ROOT/pics/posters/2026"
WORK_DIR="$(mktemp -d)"
DRIVE_FOLDER="https://drive.google.com/drive/folders/1eb9h1DQhA8eaNP_53kPgdF13X1lEvhrX"

mkdir -p "$OUT_DIR" "$WORK_DIR/pdf" "$WORK_DIR/png"

cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

if ! command -v gdown >/dev/null 2>&1; then
  echo "Install gdown: pip install gdown" >&2
  exit 1
fi

gdown --folder "$DRIVE_FOLDER" -O "$WORK_DIR"

declare -A SLUG=(
  ["Poster 1 StaticAnalyzer"]="static-analyzer"
  ["Poster 2 MatrixCore"]="matrix-core"
  ["Poster 3 TALU"]="talu"
  ["Poster 4 ETComparator"]="et-comparator"
  ["Poster 5 CoDMA"]="codma"
  ["Poster 6 DMX"]="dmx"
  ["Poster 7 SpGEMM"]="spgemm"
  ["Poster 8 SuperscalarRV"]="superscalar-rv"
)

for pptx in "$WORK_DIR"/*.pptx; do
  base=$(basename "$pptx" .pptx)
  slug="${SLUG[$base]:-}"
  if [[ -z "$slug" ]]; then
    echo "No slug mapping for: $base" >&2
    exit 1
  fi
  libreoffice --headless --convert-to pdf --outdir "$WORK_DIR/pdf" "$pptx"
  pdf="$WORK_DIR/pdf/${base}.pdf"
  pdftoppm -png -f 1 -l 1 -r 144 "$pdf" "$WORK_DIR/png/$slug"
  png=$(ls "$WORK_DIR/png/${slug}"-*.png | head -1)
  convert "$png" -quality 85 -define webp:method=6 "$OUT_DIR/${slug}.webp"
  echo "Wrote $OUT_DIR/${slug}.webp"
done
