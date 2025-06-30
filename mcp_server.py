#This Server will reverse a string and also number

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def echo():
    data = request.json
    user_message = data.get('message', '')
    return jsonify({
        'response': f"MCP Server says: '{user_message[::-1]}'"
    })

if __name__ == '__main__':
    app.run(port=5001)
