#!/bin/bash

npm install -g newman
newman run Postman_cli-Newman/sample-collection.json -r json --reporter-json-export Postman_cli-Newman/report.json