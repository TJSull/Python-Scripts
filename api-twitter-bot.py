import json
import requests
import time
import tweepy


def bitcoin():
	btc = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc")
	btc.text
	btcprice = json.loads(btc.text)
	price = btcprice['result'][0]['Last']
	return str(price)

def decred():
	dcr = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-dcr")
	dcr.text
	dcrprice = json.loads(dcr.text)
	price = dcrprice['result'][0]['Last']
	return str(price)

def ethereum():
	eth = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-eth")
	eth.text
	ethprice = json.loads(eth.text)
	price = ethprice['result'][0]['Last']
	return str(price)

#Authentication keys needed to associate and authenticate with Twitter
#Keys have been left blank for GitHub
CONSUMER_KEY = 'insert-here'
CONSUMER_SECRET = 'insert-here'
ACCESS_KEY = 'insert-here'
ACCESS_SECRET = 'insert-here'

#Use Tweepy to authenticate with Twitter and update status
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    api.update_status(status="Bitcoin Current Price: " + bitcoin() + "\nDecredit Current Price: " + decred() + "\nEthereum Current Price: " + ethereum())

    time.sleep(1800)

#api.update_status(status="Decredit Current Price: " + decred())
#api.update_status(status="Ethereum Current Price: " + ethereum())
