#!/bin/bash
# One-time per clone: installs the pre-push gate hook.
set -e
cd "$(git rev-parse --show-toplevel)"
cp scripts/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
echo "Installed pre-push hook. Every 'git push' now runs scripts/gate-check.py first."
