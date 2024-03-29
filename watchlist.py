import requests
import os
import time
import signal
from requests.exceptions import ConnectionError, ReadTimeout

BASE_URL = 'https://api.iextrading.com/1.0/tops/last/?symbols='
SYMBOLS_FILE = '/home/pi/devel/PiWatchlist/symbols.txt'
LED_CONTROL_EXE = '/home/pi/devel/PiWatchlist/ledController '

initialValue = 0


class Watchlist:

    stocks = {}  # {symbol : shares owned}
    initialValue = 0

    def __init__(self, stocks, value):
        for stock in stocks:
            self.stocks.update({stock[0] : stock[1]})
        self.initialValue = value

    def symbols(self):
        return self.stocks.keys()


def buildUrl(watchlist):
    url = BASE_URL
    for symbol in watchlist:
        url += (symbol + ',')

    return url[:len(url) - 1]


def processWatchlist(filename):
    watchlist = []
    with open(filename, 'r') as f:
        value = 0
        for line in f:
            split = line.split()
            amount = 0
            for i in range(1, len(split), 2):
                value += int(split[i]) * float(split[i + 1])
                amount += int(split[i])

            watchlist.append((split[0], amount))

    return Watchlist(watchlist, value)


def sigterm_handler(signal, frame):
    print('Shutting Down...')
    os.system(LED_CONTROL_EXE + 'flash')
    exit(0)


signal.signal(signal.SIGTERM, sigterm_handler)

watchlist = processWatchlist(SYMBOLS_FILE)

while True:
    try:
        response = requests.get(buildUrl(watchlist.symbols()), timeout=10).json()

        currentValue = 0
        for stock in response:
            currentValue += watchlist.stocks[stock['symbol']] * float(stock['price'])

        diff = currentValue - watchlist.initialValue
        pctChange = 100 * (currentValue - watchlist.initialValue) / watchlist.initialValue

        command = ''
        if diff >= 0:
            command = LED_CONTROL_EXE + 'green'
        else:
            command = LED_CONTROL_EXE + 'red'

        os.system(command)
        time.sleep(2)

    except KeyboardInterrupt:
        print("Shutting down...")
        os.system(LED_CONTROL_EXE + 'flash')
        exit(0)

    except (ConnectionError, ReadTimeout):
        os.system(LED_CONTROL_EXE + 'flash')
        time.sleep(2)


