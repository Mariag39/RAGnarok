#!/bin/sh

pip3 install -r requirements.txt

ROOT_DIR="'$PWD'"
 

FILE=ragnarok.py
if [ -f "$FILE" ];
then
	chmod +x ragnarok.py
	mv ragnarok.py ragnarok
fi

sed -i '/^import os/a ROOT_DIR='$ROOT_DIR ragnarok


mkdir -p ~/bin

cp ragnarok ~/bin
cp dependency-check/ ~/bin

export PATH="$PATH:$HOME/bin"

echo 'export PATH=$PATH":$HOME/bin"' >> .profile
