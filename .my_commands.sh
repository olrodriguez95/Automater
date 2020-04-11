#!/bin/zsh

function create() {
    cd
    source .env
    python3 create.py $1
    cd $FILEPATH
    cd $1
    git init
    git remote add origin https://github.com/$UNAME/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}