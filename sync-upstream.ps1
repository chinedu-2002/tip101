# Sync your fork with the original (upstream) repository
# Usage: Run this script in your repo root to fetch and merge changes from upstream, then push to your fork

git fetch upstream

git checkout main

git merge upstream/main

git push origin main
