# 📥 ClipLoot — Video Downloader

### Paste. Download. Save.

Your videos, just a few clicks away.

**ClipLoot** is a responsive web-based video downloader designed to make downloading online video content straightforward. Users can enter a video URL, initiate the download, and retrieve the resulting video file through a simple web interface.

Built using **Python, Flask, JavaScript, and yt-dlp**, ClipLoot combines a lightweight web interface with a Python-powered backend to handle video extraction, downloading, and file delivery.

---

## 🚀 Features

- 🔗 **Video URL Input** — Enter a video URL through the web interface to initiate a download.
- 📥 **Video Downloading** — Uses `yt-dlp` to extract and download available video content.
- 🎥 **Best Available Quality** — Configured to select the best available video and audio streams.
- 🔊 **Audio & Video Merging** — Uses FFmpeg to merge separate video and audio streams.
- 📦 **MP4 Output** — Configures downloaded videos to be merged into MP4 format.
- ⚡ **Backend Processing** — Handles video extraction and downloading through Flask routes.
- 📁 **Download Management** — Stores downloaded files in a dedicated `downloads/` directory.
- ⬇️ **File Download** — Provides a download endpoint to retrieve processed video files.
- 🚫 **Error Handling** — Returns informative error responses for missing URLs and download failures.
- 📱 **Responsive Interface** — Provides a web interface designed for different screen sizes.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend application logic |
| Flask 3.1.2 | Web framework and HTTP routing |
| JavaScript | Frontend interactions |
| HTML5 | Web interface structure |
| CSS3 | Styling and responsive layouts |
| yt-dlp | Video extraction and downloading |
| FFmpeg | Audio and video merging |
| Gunicorn | Production WSGI server |

---

## 📂 Project Structure

```text
ClipLoot/
│
├── static/                  # Static frontend assets
│
├── templates/               # Flask HTML templates
│
├── downloads/               # Downloaded video files (generated)
│
├── app.py                   # Main Flask application
│
├── requirements.txt         # Python dependencies
│
└── .gitignore               # Git ignored files
```

---

## ⚙️ How It Works

### 1️⃣ Application Initialization

- Flask initializes the web application through `app.py`.
- The root route (`/`) renders the main HTML interface.
- The application creates a dedicated `downloads/` directory if it does not already exist.

### 2️⃣ Video URL Submission

- Users enter a video URL through the web interface.
- The frontend submits the URL to the Flask backend.
- The backend receives the request through the `/download` POST endpoint.
- The application checks whether a valid URL has been provided.

### 3️⃣ Video Extraction & Downloading

- The backend uses `yt-dlp` to extract information from the submitted URL.
- A unique identifier is generated for the downloaded file.
- The downloader is configured to select the best available video and audio streams.
- Playlist downloading is disabled to process individual videos.

### 4️⃣ Audio & Video Processing

- FFmpeg handles the merging of separate video and audio streams.
- The output format is configured as MP4.
- The processed file is stored inside the `downloads/` directory.

### 5️⃣ Download Response

- After a successful download, the backend returns a JSON response containing the filename and download URL.
- The frontend can use the returned download URL to retrieve the generated file.
- Downloaded files are served through the `/downloads/<filename>` route.

### 6️⃣ Error Handling

- Missing video URLs are handled with an appropriate error response.
- `yt-dlp` download errors are caught and returned to the frontend.
- Additional exceptions are handled to prevent unexpected failures from going unreported.

---

## ▶️ Installation & Setup

### Prerequisites

Make sure you have the following installed:

- Python 3.10 or later
- pip (Python Package Manager)
- Git
- FFmpeg
- Visual Studio Code or another code editor

### 1. Clone the Repository

```bash
git clone https://github.com/tapobrata2002/ClipLoot.git
```

### 2. Navigate to the Project Directory

```bash
cd ClipLoot
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Install & Configure FFmpeg

FFmpeg is required to merge downloaded video and audio streams.

Install FFmpeg and make sure it is accessible on your system.

**Important:** The current application specifies the following Windows FFmpeg path in `app.py`:

```python
FFMPEG_PATH = r"C:\ffmpeg\bin"
```

If FFmpeg is installed in a different location, update this path to match your installation.

### 7. Start the Flask Application

```bash
python app.py
```

### 8. Open the Application

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

You can now use ClipLoot through its web interface.

---

## 🌐 Deployment

ClipLoot uses **Flask** as its backend framework and includes **Gunicorn** as a production WSGI server dependency.

The application can be deployed on a Python-compatible hosting platform.

Before deployment, make sure to:

- Configure the FFmpeg executable path for the hosting environment.
- Ensure FFmpeg is installed and accessible.
- Configure a writable directory for downloaded files.
- Use a production WSGI server such as Gunicorn.
- Verify that the hosting platform supports the processing time and storage requirements of video downloads.

**Note:** The current backend uses a Windows-specific FFmpeg path, so deployment on Linux-based hosting requires updating the configuration.

---

## 🔮 Future Improvements

- Introduce video quality selection before downloading.
- Add support for additional output formats.
- Display video title, thumbnail, and metadata before downloading.
- Implement download progress tracking.
- Add download history and file management.
- Introduce automatic cleanup of previously downloaded files.
- Improve download status notifications and error messages.
- Add configurable FFmpeg paths instead of hardcoded locations.
- Enhance frontend responsiveness and user experience.

---

## 🤝 Contribution

This repository serves as a practical development project focused on Python backend development, Flask, third-party library integration, and video processing.

Suggestions, feedback, and improvements are welcome.

If you find something worth improving, feel free to open an issue or submit a pull request.

---

## 👨‍💻 Author

**Tapobrata Roy**

Frontend Developer | Full-Stack Developer

- GitHub: [tapobrata2002](https://github.com/tapobrata2002)

---

### 📥 CLIPLOOT

**Paste. Download. Save.**
