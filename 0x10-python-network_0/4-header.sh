#!/bin/bash
# sends GET request,header variable X-School-User-Id must be sent with  value 98
curl -sL -H 'X-School-User-Id: 98' "$1"
