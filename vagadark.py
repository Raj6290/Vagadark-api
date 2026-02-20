from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/VagaDark', methods=['GET'])
def custom_api():
    number = request.args.get('num')
    if not number:
        return jsonify({"error": "Number missing!"}), 400

    target_url = "https://number-info-for-my-rasmalai-ayushi.vercel.app/NumberByAyush"
    params = {"Number": number, "key": "Jonathan"}
    
    try:
        response = requests.get(target_url, params=params)
        return jsonify(response.json())
    except:
        return jsonify({"error": "Original API Down"}), 500

if __name__ == "__main__":
    app.run()
