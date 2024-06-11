from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.json.get('code')
    exec_locals = {}
    exec(code, {}, exec_locals)
    return jsonify(exec_locals)

if __name__ == '__main__':
    app.run(debug=True)
