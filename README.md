# Python-Scripts
Simple Python scripts. Working on learning the basics. Data sending, data retrieval, and API are the current focus of my learning.

api-twitter-bot.py - 2.29.2016
- Test account available to preview bot here: https://twitter.com/AltCoinPrice
- Reads the api from Bittrex and posts the current prices of of Bitcoin, Decred, and Ethereum to a twitter account
- Imports Tweepy, a third party Twitter Library for Python, to interact with Twitter
- The functions from bittrex-api-reader.py reader were used and modified to return a string
- Uses time function to pause and return a tweet every 30 minutes

bittrex-api-reader.py - 2.24.2016
- Developed a simple program to read the api from bittrex.com
- Displays the prices of Bitcoin, Decred, and Ethereum
- I plan on developing this further and learning more uses of API






To Do - 2.15.2016
- Create a function to send a continuously growing packet to any user defined port 
- Develop a program to serve a file on any user defined port
- Develop a program to parse HTTP headers from a webserver, return them, and save them to a text file. Possibly check multiple ports for a webserver (eg 80 and 443)
