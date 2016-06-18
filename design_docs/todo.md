Look into: http://dev.markitondemand.com/MODApis/

Make the API work: (look into jQuery and ajax requests)
https://github.com/markitondemand/DataApis/blob/master/MarkitQuoteServiceSample.js

NOTE: limit # of requests/sec or else you'll get blocked (but AWS uses multiple IPs? idk)

LOOKUP:

Send: stock ticker or part of it
Receive: ticker, name, and exchange it's in

example of lookup to get in xml format
http://dev.markitondemand.com/MODApis/Api/v2/Lookup?input=aapl

example of lookup to get in json format (preferred)
http://dev.markitondemand.com/MODApis/Api/v2/Lookup/json?input=aapl

NOTE--these query results will include results that have "aapl" in any part of the result
NOTE-- probably will not use this command except to maybe see what exchange something is traded in

QUOTE:

Probably what we'll use most of the time (best for realtime data)

Send: stock ticker (symbol)
Receive:  Status of quote request
          Name of the company
          The company's ticker symbol
          The last price of the company's stock
          The change in price of the company's stock since the previous trading day's close
          The change percent in price of the company's stock since the previous trading day's close
          The last time the company's stock was traded in exchange-local timezone. Represented as ddd MMM d HH:mm:ss UTCzzzzz yyyy
          The last time the company's stock was traded in exchange-local timezone. Represented as an OLE Automation date
          The company's market cap
          The trade volume of the company's stock
          The change in price of the company's stock since the start of the year
	        The change percent in price of the company's stock since the start of the year
          The high price of the company's stock in the trading session
          The low price of the company's stock in the trading session
          The opening price of the company's stock at the start of the trading session

Sample request: http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol=aapl
Sample result: {"Status":"SUCCESS","Name":"Apple Inc","Symbol":"AAPL",
                "LastPrice":97.64,"Change":0.5,"ChangePercent":0.514721021206506,
                "Timestamp":"Thu Jun 16 15:27:04 UTC-04:00 2016",
                "MSDate":42537.6437962963,"MarketCap":534815777000,"Volume":2907805,
                "ChangeYTD":105.26,"ChangePercentYTD":-7.2392171765153,
                "High":97.68,"Low":96.07,"Open":96.43}

NOTE-- 1 to 3 minute delay before updating

## Historical Data

Source for historical data: https://www.quandl.com/data/WIKI?keyword=
This contains 3000 stocks, not exclusive, but can find other sources to compliment.
Google csv API for historical data: http://www.google.com/finance/historical?q=TSLA&startdate=Nov%201,%202013&enddate=Nov%2030,%202015&output=csv



INTERACTIVE CHART:

Pretty complicated request, idk if we'll use it but it looks pretty cool
