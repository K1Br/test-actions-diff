#!/bin/bash
set -e
git diff --diff-filter=ACMRT ${{ github.event.pull_request.base.sha }} ${{ github.sha }} -U0 | grep 'review_date:'| cut -d\  -f2 >> date_diff.csv
cat date_diff.csv
echo "GITHUB_OLD_DATE=$(echo $(head -1 date_diff.csv))" >> $GITHUB_ENV
echo "GITHUB_NEW_DATE=$(echo $(tail -1 date_diff.csv))" >> $GITHUB_ENV
