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
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5"
    }
    data = requests.get(url, headers=headers)
    return jsonify({"html":data.text})
  except Exception as e:
    return jsonify({"html":"","error": str(e)}), 400

if __name__ == "__main__":
  port = int (os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
