#! /bin/sh -eux

cat issue-numbers.lst | while read -r issue_number; do
  page=0
  while true; do
    page=$((page + 1))
    sleep 1
    gh api \
      -H "Accept: application/vnd.github+json" \
      "/repos/PowerShell/PowerShell/issues/${issue_number}/comments?per_page=100&page=${page}" \
      > "comments/issue-${issue_number}-page-${page}.json"

    if jq -er 'length == 0' < "comments/issue-${issue_number}-page-${page}.json"; then
      rm "comments/issue-${issue_number}-page-${page}.json"
      break
    fi
  done
done
