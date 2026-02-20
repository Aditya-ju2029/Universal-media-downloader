# Universal-media-downloader<br>
🚀 Universal Media Downloader

A full-stack Django web application that enables users to download media content from multiple platforms using yt-dlp.

🌍 Live Demo

🔗 Deployed on Render
https://universal-media-downloader-2gn1.onrender.com/

📌 Project Overview

Universal Media Downloader is a production-ready web application that integrates:

A custom-designed HTML/CSS frontend

A Django backend

The yt-dlp engine for media extraction

Cloud deployment using Render

The application allows users to paste a media URL and download content directly through a browser interface.

✨ Features

🎬 Multi-platform support (YouTube, Facebook, Instagram, Vimeo, 300+ sites)

📥 Direct media download via browser

🗂 Automatic file storage in structured download directory

🔐 Secure production configuration using environment variables

⚙️ Gunicorn-based production server

📦 Clean minimal dependency management

☁️ Cloud deployment ready

🛠 Tech Stack
Layer	Technology
Backend	Django (Python)
Downloader	yt-dlp
Frontend	HTML5, CSS3
Server	Gunicorn
Static Files	Whitenoise
Version Control	Git & GitHub
Deployment	Render
🏗 Project Architecture
Browser
   ↓
Django Form (POST)
   ↓
Django View
   ↓
yt-dlp Engine
   ↓
Downloads Folder
   ↓
FileResponse (Stream to User)
⚙️ Installation (Local Setup)
1️⃣ Clone Repository
git clone https://github.com/Aditya-ju2029/Universal-media-downloader.git
cd Universal-media-downloader
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Server
python manage.py migrate
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔒 Production Configuration

DEBUG = False

SECRET_KEY stored as environment variable

ALLOWED_HOSTS configured for deployment

Static files handled by Whitenoise

Gunicorn used for WSGI serving

🚀 Deployment

Deployed using:

GitHub repository

Render Web Service

Gunicorn start command:

gunicorn media_project.wsgi:application
🧠 Technical Highlights

Converted standalone Python script into scalable Django architecture

Resolved dependency conflicts during deployment

Managed Git merge conflicts and remote synchronization

Implemented secure environment-based settings

Optimized requirements file for cloud deployment

📈 Skills Demonstrated

Full-Stack Web Development

Django Backend Development

Production Deployment

Cloud Hosting Configuration

Version Control (Git)

Debugging & Dependency Management

📜 License

This project is for educational and demonstration purposes.

👨‍💻 Author

Aditya
GitHub: https://github.com/Aditya-ju2029

⭐ If You Like This Project

Give it a star on GitHub!
