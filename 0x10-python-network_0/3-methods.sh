#!/bin/bash
# CURL only methods
curl -sI "$1" | grep -i Allow | cut -d ' ' -f2-
