#!/bin/bash
time=$1
h=$(echo $time | cut -d: -f1)
m=$(echo $time | cut -d: -f2)
s=$(echo $time | cut -d: -f3)
total_seconds=$((h * 3600 + m * 60 + s))
printf "%02d" $total_seconds
