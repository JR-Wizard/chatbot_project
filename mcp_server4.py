#This Server will give emojis based on the input

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mcp4', methods=['POST'])
def emoji_reply():
    data = request.json
    msg = data.get("message", "").strip()

    # Try to interpret the message as an integer
    if msg.isdigit():
        num = int(msg)
        if num % 2 == 0:
            response = f"🔢 {num} is an even number! ✨"
        else:
            response = f"🔢 {num} is an odd number! 🎯"
    else:
        # Not a number — decorate the string with emojis
        response = f"💬✨ {msg} 😄🎉"

    return jsonify({f"response": f"SERVER 4 says  :  {response}"})

if __name__ == '__main__':
    app.run(port=5004)
