#!/bin/bash
if hyprctl clients | grep -q "kitty-scratch"; then
    hyprctl dispatch togglespecialworkspace terminal
else
    kitty --class kitty-scratch &
fi
