#!/bin/bash

npm install -g newman
cd Postman_cli-Newman
newman run sample-collection.json -r cli,json --reporter-json-export /report.json