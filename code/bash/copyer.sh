#!/bin/bash

# Location of this script
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# FEDB is two directories up
export FEDBDIR="$( cd "$SCRIPTDIR/../.." >/dev/null 2>&1 && pwd )"

echo "🚀 Starting file sync watcher at $(date '+%Y-%m-%d %H:%M:%S')"
echo "   FEDBDIR   = $FEDBDIR"
echo "   Watch list = $FEDBDIR/code/bash/whattocopy.txt"
echo "   Target     = /tmp/astuff"
echo "-------------------------------------------------------------"

# Create base target directory
mkdir -p /tmp/astuff
echo "📁 Target base directory ready at /tmp/astuff"

# Ensure all target directories exist (from the list)
echo "📂 Creating initial directory structure..."
while IFS= read -r f || [[ -n "$f" ]]; do
    if [[ -n "$f" && ! "$f" =~ ^# ]]; then
        mkdir -p "/tmp/astuff/$f"
        echo "   ✅ Created: /tmp/astuff/$f"
    fi
done < "$FEDBDIR/code/bash/whattocopy.txt"
echo "✅ Initial directory structure ready."

# Change to project root
cd "$FEDBDIR" || { echo "❌ Failed to cd into $FEDBDIR"; exit 1; }
echo "📍 Working directory: $(pwd)"

echo "👀 Starting inotifywait monitor..."
echo "    Watching for: modify, create, move, close_write"
echo "    Any detected change → full rsync of all listed paths"
echo "-------------------------------------------------------------"

# Main monitoring loop
inotifywait -m -r -q -e modify,create,move,close_write \
  --fromfile="$FEDBDIR/code/bash/whattocopy.txt" | \
while read -r directory events filename; do
    echo "🔄 [$(date '+%H:%M:%S')] Change detected!"
    echo "    Directory : $directory"
    echo "    Events    : $events"
    echo "    File      : ${filename:-<directory event>}"

    echo "    📤 Starting rsync (with trailing slash fix)..."

    rsync_start=$(date +%s)

    while IFS= read -r f || [[ -n "$f" ]]; do
        if [[ -n "$f" && ! "$f" =~ ^# ]]; then
            echo "       → Syncing contents of: $f/"
            # Important: trailing slash on source
            rsync -av "$f/" "/tmp/astuff/$f/" | tail -n 8
        fi
    done < "$FEDBDIR/code/bash/whattocopy.txt"

    rsync_end=$(date +%s)
    echo "    ✅ Rsync completed in $((rsync_end - rsync_start)) seconds"
    echo "    📦 All watched paths synchronized at $(date '+%Y-%m-%d %H:%M:%S')"
    echo "-------------------------------------------------------------"
done
