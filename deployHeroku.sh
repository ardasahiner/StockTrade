# Ensure directory vStockAnalytics is in the same root directory
# Ensure directory vStockAnalytics is set up with git uplink url

# Use this shell script to automatically deploy to heroku

cd ..

if [ ! -d "vStockAnalytics" ]; then
  mkdir vStockAnalytics/
fi

cp -r StockTrade/* vStockAnalytics/
cd vStockAnalytics/

git add --all
git commit -m "Deploying to Heroku"
git push heroku master
