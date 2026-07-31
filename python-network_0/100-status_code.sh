#!/bin/bash
# Displays only the status code of the response without using pipes or redirections
curl -s -o /dev/null -w "%{http_code}" "$1"
