#!/bin/bash
# usage: fetch_arxiv_pdf.sh basedir id...   (each PDF into its own directory)
base="$1"; shift
for id in "$@"; do
  d="$base/$(echo "$id" | tr '/' '_')"
  mkdir -p "$d"
  if [ ! -s "$d/paper.pdf" ]; then
    curl -sS -L -m 120 -A "Mozilla/5.0 (referee audit)" -o "$d/paper.pdf" "https://arxiv.org/pdf/$id"
  fi
  printf "%s %s\n" "$id" "$(file -b "$d/paper.pdf" | cut -c1-40) $(stat -c %s "$d/paper.pdf")"
done
