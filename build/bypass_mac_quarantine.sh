#!/bin/bash
APP="/Applications/MacFoxes68k.app"
if [ ! -d "$APP" ]; then
  echo "Drag app to your Applications folder first, then run this again."
  read -p "Press Enter to close."
  exit 1
fi
xattr -dr com.apple.quarantine "$APP"
echo "Done. App is no longer blocked by macOS Gatekeeper."
echo "Close this window and launch Binary from Applications."
sleep 3
