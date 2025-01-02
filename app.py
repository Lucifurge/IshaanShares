from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Cookie storage for validation (you can store these in a database or a more permanent solution in production)
cookies_storage = []

# Helper function to validate the cookies
def is_valid_cookie(cookie):
    required_keys = ["dbln", "sb", "ps_l", "ps_n", "datr", "locale", "c_user", "wd", "fr", "xs"]
    return all(key in cookie for key in required_keys)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    service_type = data.get('serviceType')
    fbstate = data.get('fbstate')
    url = data.get('url')
    amount = data.get('amount')
    interval = data.get('interval')
    cookies = data.get('cookies')

    # Check if all required fields are present
    if not all([service_type, fbstate, url, amount, interval, isinstance(cookies, list)]):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate cookies
    for cookie in cookies:
        if is_valid_cookie(cookie):
            cookies_storage.append(cookie)

    # Ensure valid range for amount and interval
    if not (1 <= amount <= 1000000):
        return jsonify({'error': 'Amount must be between 1 and 1 million'}), 400
    if not (1 <= interval <= 60):
        return jsonify({'error': 'Interval must be between 1 and 60'}), 400

    # Simulate sharing action (delay based on amount and interval)
    # In reality, you would implement the logic to interact with Facebook's API or your tool
    result = f"{amount} shares completed in intervals of {interval} seconds"

    # Simulate a delay for shares, for demonstration purposes
    # In reality, you would replace this with actual logic to perform the shares
    # Simulate delay here if necessary (using sleep or a similar method)
    
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Running on localhost port 5000
