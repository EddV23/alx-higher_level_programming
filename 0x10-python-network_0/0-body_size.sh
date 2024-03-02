#!/bin/bash
# takes in URL, sends request to URL, displays size of the body of the response
curl -s "$1" | wc -c
