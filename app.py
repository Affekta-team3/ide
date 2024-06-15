from flask import Flask, request, jsonify
from flask_cors import CORS
import io
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/execute', methods=['POST'])
def execute_code():
    data = request.get_json()
    code = data.get('code', '')

    try:
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout
        
        # Execute the code
        exec(code, {}, {})
        
        # Reset stdout and capture output
        sys.stdout = old_stdout
        result = new_stdout.getvalue()

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
