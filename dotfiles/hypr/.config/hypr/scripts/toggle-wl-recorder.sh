#!/bin/bash

if pgrep -x wl-recorder > /dev/null; then
    pkill wl-recorder
    notify-send "Screen Recording" "Recording saved to ~/Videos/Recordings/"
else
    choice=$(printf "Fullscreen\nRegion" | rofi -dmenu -p "Record")

    if [ -z "$choice" ]; then
        exit 0
    fi

    mkdir -p "$HOME/Videos/Recordings"

    if [ "$choice" = "Fullscreen" ]; then
        wl-recorder -f "$HOME/Videos/Recordings/$(date +%Y%m%d_%H%M%S).mp4" &
        notify-send "Screen Recording" "Recording started (Fullscreen)"
    elif [ "$choice" = "Region" ]; then
        geom=$(slurp)
        if [ -z "$geom" ]; then
            exit 0
        fi
        wl-recorder -g "$geom" -f "$HOME/Videos/Recordings/$(date +%Y%m%d_%H%M%S).mp4" &
        notify-send "Screen Recording" "Recording started (Region)"
    fi
fi
