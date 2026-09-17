#!/bin/sh
# Requires fontconfig, woff2_decompress, and librsvg (rsvg-convert).
set -eu
root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT HUP INT TERM
mkdir "$work/fonts" "$work/cache"
for name in chakra-petch-bold space-grotesk-variable; do
  cp "$root/fonts/$name.woff2" "$work/fonts/"
  woff2_decompress "$work/fonts/$name.woff2"
done
printf '<?xml version="1.0"?><!DOCTYPE fontconfig SYSTEM "fonts.dtd"><fontconfig><dir>%s/fonts</dir><cachedir>%s/cache</cachedir></fontconfig>\n' "$work" "$work" > "$work/fonts.conf"
FONTCONFIG_FILE="$work/fonts.conf" rsvg-convert "$root/img/sunshinectf26-social.svg" -o "$root/img/sunshinectf26-social.png"
