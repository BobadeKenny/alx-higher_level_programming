#!/bin/bash
# sends a JSON POST request
curl -s -X POST "$1" -d @"$2" --header "Content-Type: application/json"
