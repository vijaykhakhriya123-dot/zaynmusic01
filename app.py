from flask import Flask, request, jsonify
from pytubefix import YouTube
import os

app = Flask(__name__)

# Render ke environment variable se cookie uthayenge
ROBLOX_COOKIE = os.environ.get("ROBLOX_COOKIE")

@app.route('/')
def home():
    return "Zayn Music Backend is Live! 🎵"

@app.route('/upload', methods=['POST'])
def upload_music():
    try:
        data = request.json
        if not data or 'url' not in data:
            return jsonify({"success": False, "error": "No URL provided"}), 400

        yt_url = data.get('url')
        print(f"Downloading started for: {yt_url}")

        # 🚀 THE ULTIMATE BYPASS: pytubefix with PO Token
        # Yeh YouTube ke anti-bot system ko hara dega
        yt = YouTube(yt_url, use_po_token=True)
        
        # Sirf audio stream extract karna (Fastest method)
        audio_stream = yt.streams.get_audio_only()
        
        # Audio ko server par download karna
        audio_stream.download(filename="music.m4a")
        
        print("Download successful!")

        # Yahan Roblox API par upload karne ka code aayega
        generated_asset_id = "1234567890" # Dummy ID for testing

        # Space bachane ke liye download ke baad delete
        if os.path.exists("music.m4a"):
            os.remove("music.m4a")

        return jsonify({
            "success": True, 
            "asset_id": generated_asset_id, 
            "message": "Uploaded successfully to Zayn Hub!"
        })

    except Exception as e:
        print("ERROR AAYA HAI:", str(e))
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
