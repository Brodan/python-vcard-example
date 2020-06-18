#!/bin/bash
curl -X POST https://api.twilio.com/2010-04-01/Accounts/<ACCOUNT_SID>/Messages.json \
--data-urlencode "Body=Mmm... donuts." \
--data-urlencode "MediaUrl=<YOUR NGROK URL>/HomerSimpson.vcf" \
--data-urlencode "From=+15555555555" \
--data-urlencode "To=+15555555555" \
-u <ACCOUNT_SID>:<AUTH_TOKEN>
