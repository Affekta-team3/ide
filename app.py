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

    old_stdout = sys.stdout
    sys.stdout = new_stdout = io.StringIO()

    try:
        exec(code, {}, {})
        
        output = new_stdout.getvalue()
        sys.stdout = old_stdout

        return jsonify({"result": output.strip()})  # Strip to remove any extraneous whitespace
    except SyntaxError as e:
        sys.stdout = old_stdout
        return jsonify({"error": f"SyntaxError: {e.msg} at line {e.lineno}, column {e.offset}"})
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
