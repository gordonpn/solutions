#!/bin/bash
# Converting - to _ in all files in current directory.

for i in *-*; do
  [[ -e "$i" ]] || break
  echo "$i"
  NEW=$(echo "$i" | tr '-' '_')
  mv "$i" "$NEW"
done
