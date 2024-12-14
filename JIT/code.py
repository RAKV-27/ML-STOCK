from flask import Flask, request, jsonify
import yfinance as yf
from datetime import datetime

app = Flask(__name__)

@app.route('/api/fetch_stock_data', methods=['GET'])
def fetch_stock_data():
    symbol = request.args.get('symbol')
    start = request.args.get('start')
    end = request.args.get('end')

    try:
        data = yf.download(symbol, start=start, end=end)
        response = {
            "data": [
                {"date": index.strftime("%Y-%m-%d"), "close": row["Close"]}
                for index, row in data.iterrows()
            ]
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/predict_stock_trends', methods=['GET'])
def predict_stock_trends():
    # Placeholder prediction logic
    symbol = request.args.get('symbol')

    # Replace with your AI prediction modela
    prediction_data = [
        {"date": (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d"), "price": 100 + i}
        for i in range(1, 31)
    ]
    return jsonify({"data": prediction_data})

if __name__ == '__main__':
    app.run(debug=True)
