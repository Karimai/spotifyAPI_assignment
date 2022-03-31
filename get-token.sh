#!/usr/bin/env bash
#curl -X POST -d "client_id=$1&client_secret=$2&grant_type=client_credentials" https://accounts.spotify.com/api/token

# python3 main.py -i client_id -s client_secret
python3 main.py -i $1 -s $2
# python3 ./main.py -i 732347158c784230bc0b0dadabd43daf -s 16d9218fc9bd479992f51ff89fbc2b4b

