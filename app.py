from flask import Flask, render_template, request, send_from_directory, jsonify
import yt_dlp
import os
import uuid

FFMPEG_PATH = r"C:\ffmpeg\bin"

app = Flask(__name__)

# Folder where downloaded videos will be stored
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "downloads")
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download", methods=["POST"])
def download():
    try:
        url = request.form.get("url")

        if not url:
            return jsonify({"success": False, "error": "Please enter a video URL."})

        file_id = str(uuid.uuid4())

        output_template = os.path.join(DOWNLOAD_FOLDER, f"{file_id}.%(ext)s")

        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "outtmpl": output_template,
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
            "merge_output_format": "mp4",
            "ffmpeg_location": FFMPEG_PATH,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            downloaded_file = ydl.prepare_filename(info)

        filename = os.path.basename(downloaded_file)

        if not os.path.exists(downloaded_file):
            return jsonify(
                {"success": False, "error": "Download failed. File was not created."}
            )

        return jsonify(
            {
                "success": True,
                "filename": filename,
                "download_url": f"/downloads/{filename}",
            }
        )

    except yt_dlp.utils.DownloadError as e:
        return jsonify(
            {"success": False, "error": f"Unable to download this video: {str(e)}"}
        )

    except Exception as e:
        return jsonify({"success": False, "error": f"Something went wrong: {str(e)}"})


@app.route("/downloads/<filename>")
def serve_download(filename):
    return send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)


if __name__ == "__main__":
    # app.run(debug=True, host="127.0.0.1", port=5000)
    import os

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
