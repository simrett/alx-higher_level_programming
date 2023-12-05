#!/bin/bash
# displays request status from server
curl -s -o /dev/null -I -w "%{http_code}" "$1"
