#!/bin/bash
# sends GET request,header variable X-School-User-Id must be sent with  value 98
curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
