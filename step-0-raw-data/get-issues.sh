#! /bin/sh -eux

page=0
while true; do
  page=$((page + 1))
  sleep 2
  gh api \
    -H "Accept: application/vnd.github+json" \
    "/repos/PowerShell/PowerShell/issues?state=all&per_page=100&page=${page}" \
    > "issues/${page}.json"
done
