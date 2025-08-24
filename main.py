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
  if url == "":
    return jsonify({"html":"","error":"Please provide the URL"}), 400
  elif url == "about:blank":
    return jsonify({"html":""})
  else:
    try:
      headers = {
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "Accept-Encoding": "gzip, deflate, br, zstd, dcb, dcz",
          "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5",
          "Cache-Control": "max-age=0",
          "Available-Dictionary": ":t6/pLuDxmzbud3XIzdKZonuYhmRI0vXiAzANyKWwv94=:",
          "Sec-Ch-Ua-Form-Factors": "Desktop",
          "Sec-Ch-Ua-Platform": "Windows",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
      }
      data = requests.get(url, headers=headers)
      return jsonify({"html":data.text})
    except Exception as e:
      return jsonify({"html":"","error": str(e)}), 400
      
@app.route("html", methods=['GET'])
def api():
  url = request.args.get('site')
  if url == "":
    return ("Please provide the URL"), 400
  elif url == "about:blank":
    return ("")
  else:
    try:
      headers = {
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
          "Accept-Encoding": "gzip, deflate, br, zstd, dcb, dcz",
          "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5",
          "Cache-Control": "max-age=0",
          "Available-Dictionary": ":t6/pLuDxmzbud3XIzdKZonuYhmRI0vXiAzANyKWwv94=:",
          "Sec-Ch-Ua-Form-Factors": "Desktop",
          "Sec-Ch-Ua-Platform": "Windows",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"
      }
      data = requests.get(url, headers=headers)
      return data.text
    except Exception as e:
      return jsonify({"html":"","error": str(e)}), 400
if __name__ == "__main__":
  port = int (os.environ.get("PORT", 5000))
  app.run(host='0.0.0.0', port=port)
