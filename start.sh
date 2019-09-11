#!/bin/bash

source /home/pi/devel/PiWatchlist/watchlistEnv/bin/activate
nohup python /home/pi/devel/PiWatchlist/watchlist.py >/dev/null 2>&1 &
