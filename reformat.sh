#!/bin/bash

black app/ tests/

for file in app/static/js/*.js; do
    npx eslint $file --fix
done