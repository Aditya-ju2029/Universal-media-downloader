import yt_dlp
import os

# ==============================
# MEDIA URL
# ==============================
MEDIA_URL = "https://youtu.be/MdNCYfZBV5k?si=Tz8YPmRCzLqmq9iE"

# ==============================
# Fixed Download Folder
# ==============================
BASE_PATH = r"C:\Users\adity\OneDrive\Desktop\Internship"
DOWNLOAD_FOLDER = os.path.join(BASE_PATH, "Downloads")

# Create folder if not exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

# ==============================
# Download Settings (No FFmpeg Needed)
# ==============================
ydl_opts = {
    'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
    'format': 'best',   # Single combined format (no merging)
    'noplaylist': False,
    'quiet': False,
    'no_warnings': True
}

# ==============================
# Download Function
# ==============================
def download_media(url):
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print("Download failed:", e)

# ==============================
# Run
# ==============================
if __name__ == "__main__":
    print("Saving to:", DOWNLOAD_FOLDER)
    download_media(MEDIA_URL)
