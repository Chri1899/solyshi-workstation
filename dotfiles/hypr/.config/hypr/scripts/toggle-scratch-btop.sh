#!/bin/bash

if hyprctl clients | grep -q "kitty-btop"; then
    hyprctl dispatch togglespecialworkspace btop
else
    kitty --class kitty-btop -e btop &
fi
