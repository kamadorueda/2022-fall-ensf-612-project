#! /bin/sh -eu

find issues -type f -name '*.json' | sort | while read -r issue_json; do
  jq -r .[].number < "${issue_json}" | sort | while read -r number; do
    echo "${number}" >> issue-numbers.lst
  done
done
