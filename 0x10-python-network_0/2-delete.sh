#!/bin/bash
# sends DELETE request to URL passed as first argument,displays body of response
curl -sX DELETE "$1"
