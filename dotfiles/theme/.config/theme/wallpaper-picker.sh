#!/usr/bin/env bash
set -e

source "$HOME/.config/theme/paths.sh"

WALLPAPER=$(fd -e png -e jpg -e jpeg -e webp . "$WALLPAPER_DIR" \
  | sort \
  | rofi -dmenu -i -p "Wallpaper")

[ -z "$WALLPAPER" ] && exit 0

echo "$WALLPAPER" > "$WALLPAPER_STATE"
"$HOME/.config/theme/apply.sh"
