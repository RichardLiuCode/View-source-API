from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
  return "<h1>View source code API</h1>"

@app.route('/api', methods=['GET'])
def api():
  url = request.args.get('site')
  try:
    headers = {
        "User-Agent": "Mozilla/5.0"  # 偽裝成瀏覽器
    }
    data = requests.get(url, headers=headers)
    return jsonify({"html":data.text})
  except Exception as e:
    return "Error:" + str(e), 400

if __name__ == "__main__":
  port = int (os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
