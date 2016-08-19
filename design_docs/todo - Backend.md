NOTE: limit # of requests/sec or else you'll get blocked (but AWS uses multiple IPs? idk)

REFER TO FRONTEND FILE: frontend file (website_frontend.txt) contains all of the information pertaining to angular frontend

BACKEND tasks (as of 7/13):

Caching current stock prices in the users routes
Use Yahoo for GOOG in stocks routes (special case)
(Maybe) Caching historical prices in the stocks routes  

Later tasks:

Machine learning on stock data:

Both univariate and multivariate models
1 day, 1 month, and 1 year predictions
Whether the stock will go up or down, and whether the stock will beat the market

Try:
PCA->Logistic regression
  Find optimal lambda from cross validation set, then test on test set
SVM
  Try both with and without PCA
Neural Net
  Try both with and without PCA
  Find optimal lambda
  Try varying amounts of hidden layers, elements in each layer

Data:
  Univariate:
    Use only previous price from a given stock to attempt to make a prediction
    Pull daily price data for 300 stocks from Yahoo from past 12 years
      Need 13 years for 1 year predictions
    Research seems to show that using 2 years of previous data is sufficient
      for prediction
      This means about 700 features
    Start training on data from 10 years ago (data from 2 earlier years used as
      features)
    Training set: 10-4 years, cross validation 4-2 years, test 2-0 years
  Multivariate:
    Probably need 500 stocks for this (training set of 1,000,000 data points!)
    Include daily price data from common indexes (S&P, DJIA, NASDAQ, FTSE, etc.)
    Include info about trading volume and market cap
    Currency exchange rates data
    Look into Yahoo stock news feed--see if you can get old data and try to do
      NLP
    Probably about 5000+ features

Use F1 score to evaluate quality of classifier b/c data will be skewed upwards
Goal is to find best learning algorithm, and then when a user searches for a stock
  there will be a "Our Recommendation" button they can press. Once they press the button,
  we pull all necessary information (probably using Barchart) and run the classifier and
  return our prediction, noting our overall accuracy
Could also have a way for them to give feedback about the algorithm so it trains
as it goes as well
