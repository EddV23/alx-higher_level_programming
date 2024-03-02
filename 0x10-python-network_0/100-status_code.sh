#!/bin/bash
# sends request to URL passed as argument, displays only status code of response.
curl -s -o /dev/null -w "%{http_code}" "$1"
