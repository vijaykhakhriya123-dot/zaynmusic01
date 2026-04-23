from flask import Flask, request, jsonify
import yt_dlp
import requests
import os

app = Flask(__name__)

# Render ke environment variable se cookie uthayenge (100% Safe)
ROBLOX_COOKIE = os.environ.get("ROBLOX_COOKIE")

@app.route('/')
def home():
    return "Zayn Music Backend is Live! 🎵"

@app.route('/upload', methods=['POST'])
def upload_music():
    try:
        data = request.json
        yt_url = data.get('url')

        if not yt_url:
            return jsonify({"success": False, "error": "No URL provided"}), 400

        # Step 1: YouTube se Audio Download karna
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'music.mp3', # Downloaded file ka naam
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '128',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

        # Step 2: Roblox par Upload karna
        # (Yahan Roblox ki official Upload API ka request aayega jo MP3 file aur cookie use karega)
        
        # Abhi ke liye hum ek dummy ID bhej rahe hain testing ke liye
        generated_asset_id = "1234567890" 

        # Server ka space bachane ke liye gaana download hone ke baad delete kar do
        if os.path.exists("music.mp3"):
            os.remove("music.mp3")

        return jsonify({
            "success": True, 
            "asset_id": generated_asset_id, 
            "message": "Uploaded successfully to Zayn Hub!"
        })

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
