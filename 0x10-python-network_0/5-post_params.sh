#!/bin/bash
# sends POST request, variable email must be sent with the value test@gmail.com
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
