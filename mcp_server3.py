#This Server checks palindrome for string and positive or negative for number

from flask import Flask, request, jsonify

app = Flask(__name__)

def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

@app.route('/mcp3', methods=['POST'])
def process_message():
    data = request.json
    msg = data.get("message", "").strip()

    # Check if it's a number 
    try:
        num = float(msg)
        if num > 0:
            response = f"{num} is a positive number."
        elif num < 0:
            response = f"{num} is a negative number."
        else:
            response = f"{num} is zero."
        return jsonify({"response": f"SERVER 3 says  : {response}"})
    except ValueError:
        #check for palindrome
        if is_palindrome(msg):
            return jsonify({"response": f"SERVER 3 says : '{msg}' is a palindrome."})
        else:
            return jsonify({"response": f"SERVER 3 says  : '{msg}' is not a palindrome."})

if __name__ == '__main__':
    app.run(port=5003)
