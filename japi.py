def getStockDate():
    import urllib.request
   
    symbol = input("Enter a stock symbol or quit to exit: ")
    if symbol != "quit":
        nasdaqURL = 'https://www.alphavantage.co/query?\
        function=TIME_SERIES_INTRADAY&symbol="""symbol"""&\
        apikey=0V7YKE06WI20CADD'
        connection = urllib.request.urlopen(nasdaqURL)
        responseString = connection.read().decode()
        print (responseString)
        responseString = {}
        print (responsestring.keys(4))
    else:
        exit
