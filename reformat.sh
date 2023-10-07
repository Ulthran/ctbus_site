#!/bin/bash

black app/ tests/

for file in app/static/js/*.js; do
    js-beautify -f $file -o $file
done