#!/usr/bin/env bash

NEW_BUCKET="nome-do-bucket"
OLD_BUCKET="nome-do-bucket"

aws s3api create-bucket --bucket $NEW_BUCKET --object-ownership ObjectWriter \

# aws s3api put-bucket-policy --bucket $NEW_BUCKET --policy file://bucket.json \

aws s3 cp s3://$OLD_BUCKET/ s3://$NEW_BUCKET/ --recursive \

aws s3 website s3://$NEW_BUCKET/ --index-document index.html --error-document index.html

aws s3 ls s3://$NEW_BUCKET --recursive | cut -c 32- | xargs -n 1  -- aws s3api put-object-acl --acl public-read --bucket $NEW_BUCKET --key
