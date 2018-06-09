#!/bin/bash

PAYLOAD=$(<payload.json)
TMPFILE=$(mktemp)
DATA="{\"ref\": \"${PAYLOAD}\"}"
SIGNATURE=$(echo -n "${DATA}" | openssl dgst -sha1 -hmac "${GITHUB_WEBHOOK_SECRET}" | awk '{print "X-Hub-Signature: sha1="$2}')
curl -X POST -H "Content-Type: application/json" -H "${SIGNATURE}" --data "${DATA}" http://0.0.0.0:9010/hooks/colour-science.org
rm -f "${TMPFILE}"
