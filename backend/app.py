from flask import Flask,request,redirect,jsonify
import yfinance as yf
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# apple = yf.Ticker("AAPL")

# stock_info = apple.info
# current_price = stock_info['currentPrice']
# print("Current price of AAPL:", current_price)

# Get stock info
# apple_info = apple.info
# print(apple_info)

# Get historical market data
# hist = apple.history(period="1mo")
# print(hist)

@app.route('/get_stock',methods=['POST'])
def get_stock():
    try:
        data = request.json
        print(data)
        ticker_symbol = data.get('ticker', 'AAPL')
        stock = yf.Ticker(ticker_symbol)


        info = stock.info
        extended_info = {
            "ticker": ticker_symbol,
            "companyName": info.get('longName', 'Unknown Company'),
            "currentPrice": info.get('currentPrice'),
            "marketCap": info.get('marketCap'),
            "forwardPE": info.get('forwardPE'),
            "dividendYield": info.get('dividendYield'),
            "fiftyTwoWeekHigh": info.get('fiftyTwoWeekHigh'),
            "fiftyTwoWeekLow": info.get('fiftyTwoWeekLow'),
            "volume": info.get('volume'),
        }

        # Fetching historical data
        hist = stock.history(period="1mo")
        historical_data = hist.to_dict(orient="records")  
        extended_info["historicalData"] = historical_data


        return jsonify(extended_info)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

