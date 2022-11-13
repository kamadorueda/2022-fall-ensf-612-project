#! /bin/sh -eux

find . -type f -name '*.json' | while read -r path; do
  jq -S < "${path}" > "${path}.2"
  mv "${path}.2" "${path}"
done
