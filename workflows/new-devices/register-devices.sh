#!/usr/bin/env bash

#######################
# Example input file:
#
# users.txt
# -----------------------------------------------------
# diego,b1f1c4bf5ea24fd4a12ef929dde8f7f5,3
# rodrigo,fff0008071d9424fb6d31affc0b727b9,4
# mario,8c24c3e31bad43f5a608122fdd7aa6f7,4
# anabel,55f498729e31488f810fa855e253cf7d,3
# camila_composed_name,b765740ebb31414ca91ab063ad08f0c8,4
# ------------------------------------------------------
################


FLEET="netrics-fleet"
BALENA_VERSION="2.12.7"

mkdir -p configs

printf '['
while IFS=',' read -r name uuid version
do
  printf '.'
  DEVICE_TYPE="raspberrypi${version}-64"

  balena device rm -y $uuid > /dev/null
  balena device register $FLEET --uuid $uuid --deviceType $DEVICE_TYPE > /dev/null
  balena device rename $uuid $name > /dev/null

  balena config generate \
	--device $uuid \
  	--version "$BALENA_VERSION" \
  	--network ethernet \
  	--output "config/$name.json" \
	--appUpdatePollInterval 15 > /dev/null

	cat "config/$name.json" jq --arg keyvar "$(cat ~/.ssh/id_rsa.pub)" '. + {"os": {"sshKeys": [$keyvar]}}' > "config/$name.json"


done < users.csv
printf ']\n'