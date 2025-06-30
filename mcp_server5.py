#This Server will give back the length of input

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mcp5', methods=['POST'])
def length_reply():
    data = request.json
    msg = data.get("message", "")
    return jsonify({"response": f"Your message has {len(msg)} characters."})

if __name__ == '__main__':
    app.run(port=5005)
