#!/usr/bin/env bash

mkdir -p flashed_images
for f in $(ls config/*.json);
do
	name=$(basename $f .json)
	dt=$(<$f jq -r '.deviceType');

	if [ "$dt" == "raspberrypi3-64" ]; then
		version="3"
	else
		version="4"
	fi
	echo "$name $dt $version"

	cp "images/rp$version.img" "$name.img"
	sudo balena config inject $f --drive "$name.img" > /dev/null
	tar -czvf "$name-$version.tar.gz" "$name.img" > /dev/null
	rm "$name.img"
	mv "$name-$version.tar.gz" flashed_images/

done