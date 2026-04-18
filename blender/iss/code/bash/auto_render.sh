#!/bin/bash
# autorender.sh - Auto-run render.sh when any file in the "code" directory changes
set -o noclobber   # or: set -C

# Location of this script
SCRIPTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
# Projectdir is two up
export PROJECTDIR="$( cd $SCRIPTDIR/../.. >/dev/null 2>&1 && pwd )"

WATCH_DIR="${PROJECTDIR}/code"
RENDER_SCRIPT="${PROJECTDIR}/code/bash/run_render.sh"
LOCKFILE="/tmp/autorender.lock"           # Lock to ensure only one render runs
DEBOUNCE_SECONDS=2                        # Wait this many seconds after last change

if ! command -v inotifywait >/dev/null 2>&1; then
    echo "Error: inotifywait not found. Install with: sudo apt install inotify-tools"
    exit 1
fi

echo "🚀 Starting auto-renderer with debounce (${DEBOUNCE_SECONDS}s) and single-instance lock"
echo "Watching: $WATCH_DIR (recursive)"
echo "Will run: $RENDER_SCRIPT"
echo "Press Ctrl+C to stop."

function do_render() {
   # Debounce: wait 2 seconds (any new changes during this time reset the timer)
    echo "⏳ Waiting ${DEBOUNCE_SECONDS} seconds for more changes..."
    sleep "${DEBOUNCE_SECONDS}"

    # Run the render script
    if "$RENDER_SCRIPT"; then
        echo "✅ Render completed successfully."
    else
        echo "❌ Render failed or was interrupted."
    fi

    # Release lock
    rm -f "$LOCKFILE"
    echo "🔓 Lock released. Ready for next change."
}

# Main watcher loop
inotifywait -m -r -q -e modify,create,move,close_write \
  --exclude '\.(swp|swx|tmp|pyc|pyo)$|__pycache__' \
  "$WATCH_DIR" | \
while read -r directory events filename; do
    echo "🔄 Change detected: $directory$filename"

    # Check if another render is already running
    if { > "$LOCKFILE"; } 2>/dev/null; then
        echo "✅ Created lockfile ($LOCKFILE)"
    else
        echo "⚠️  Another render is still running (lockfile exists). Skipping this trigger."
        continue
    fi
    echo "▶️  Starting render (lock acquired)..."

    # Run the render script
    do_render &
done

# Cleanup
rm -f "$LOCKFILE"

echo "✅ Auto-renderer stopped."
