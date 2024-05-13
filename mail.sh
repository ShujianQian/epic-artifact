#!/bin/sh

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

EMAIL_FILENAME="./email.txt"

if [ ! -f "$EMAIL_FILENAME" ]; then
    echo -e "${GREEN}Email config file does not exist, skip.${NC}"
    exit 0  # Exit with a status of 1 to indicate error
fi

exec 3< "$EMAIL_FILENAME"
read -r SENDER_EMAIL <&3
read -r SENDER_PASSWORD <&3
read -r RECEIPIENT_EMAIL <&3

echo -e "${GREEN}Sending email from $SENDER_EMAIL to $RECEIPIENT_EMAIL${NC}"

SUBJECT="Epic Artifact Evaluation Finished"

curl --ssl-reqd \
  --url 'smtps://smtp.gmail.com:465' \
  --user "$SENDER_EMAIL:$SENDER_PASSWORD" \
  --mail-from "$SENDER_EMAIL" \
  --mail-rcpt "$RECEIPIENT_EMAIL" \
  --upload-file - <<EOF
From: $SENDER_EMAIL
To: $RECEIPIENT_EMAIL
Subject: $SUBJECT

Dear $RECEIPIENT_EMAIL,

Your Epic experiment run is finished.

Epic Artifact Evaluation
EOF


