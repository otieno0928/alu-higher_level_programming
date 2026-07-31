#!/bin/bash
# Sends a GET request to the URL with a header parameter
curl -sG -H "X-HolbertonSchool-User-Id: 98" "$1"
