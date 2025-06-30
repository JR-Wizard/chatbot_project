#This Server checks prime or not for digits and also it convert string to upper case based on the

from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/mcp2', methods=['POST'])
def process_message():
    data = request.json
    user_message = data.get('message', '').strip()

    # If input is a valid number
    if user_message.isdigit():
        num = int(user_message)
        if is_prime(num):
            result = f"{num} is a prime number."
        else:
            result = f"{num} is not a prime number."
        return jsonify({'response': f"SERVER 2 says: {result}"})

    # If input is alphabetic, convert to uppercase
    return jsonify({
        'response': f"SERVER 2 says: {user_message.upper()}"
    })

if __name__ == '__main__':
    app.run(port=5002)
