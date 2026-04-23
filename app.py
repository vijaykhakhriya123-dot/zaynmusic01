from flask import Flask, request, jsonify
import yt_dlp
import os

app = Flask(__name__)

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

        # 🚀 FAST DOWNLOAD SETTINGS (No FFmpeg needed)
        ydl_opts = {
            'format': 'm4a/bestaudio/best', # Direct m4a format, bina kisi conversion ke
            'outtmpl': 'music.m4a',
            'noplaylist': True,
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        # Yahan par aapka Roblox Upload Logic aayega
        generated_asset_id = "1234567890" # Test ID

        # Server ka space clear karna
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
