#!/bin/bash
time=$1
if ! [[ $time =~ ^([0-9]{2}):([0-9]{2}):([0-9]{2})$ ]]; then
  echo "Invalid time format. Please use HH:MM:SS."
  exit 1
fi
hours=$(cut -d: -f1 <<< "$time")
minutes=$(cut -d: -f2 <<< "$time")
seconds=$(cut -d: -f3 <<< "$time")
((seconds -= 5))
if ((seconds < 0)); then
  ((minutes -= 1))
  ((seconds += 60))
  if ((minutes < 0)); then
    ((hours -= 1))
    ((minutes += 60))
  fi
fi
printf "%02d:%02d:%02d" $hours $minutes $seconds
