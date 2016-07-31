cd ..

if [ ! -d "vStockAnalytics" ]; then
  mkdir vStockAnalytics/
fi

cp -r StockTrade/* vStockAnalytics/
cd vStockAnalytics/

git add --all
git commit -m "Deploying to Heroku"
git push heroku master
