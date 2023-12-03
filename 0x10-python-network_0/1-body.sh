#!/bin/bash
# CURL to the end
curl -sLw "\n%{http_code}" -X GET "$1" -o /tmp/body_file | tail -n 1 | grep -q '^200$' && cat /tmp/body_file
