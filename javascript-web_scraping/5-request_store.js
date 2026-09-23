#!/usr/bin/node
const request = require('request');
const fs = require('fs');

request.get(process.argv[2]).pipe(fs.createWriteStream(process.argv[3], 'utf-8'));
