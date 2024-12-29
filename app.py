from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def handle_data():
    data = request.json
    return jsonify({"received": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
