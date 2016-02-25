import json
import requests


def bitcoin():
	btc = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=usdt-btc")
	btc.text
	btcprice = json.loads(btc.text)
	price = btcprice['result'][0]['Last']
	print "Bitcoin Current Price: " + str(price)

def decred():
	dcr = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-dcr")
	dcr.text
	dcrprice = json.loads(dcr.text)
	price = dcrprice['result'][0]['Last']
	print "Decredit Current Price: " + str(price)

def ethereum():
	eth = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-eth")
	eth.text
	ethprice = json.loads(eth.text)
	price = ethprice['result'][0]['Last']
	print "Ethereum Current Price: " + str(price)


bitcoin()
decred()
ethereum()

