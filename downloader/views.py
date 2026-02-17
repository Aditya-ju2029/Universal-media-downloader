import os
import yt_dlp
from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse


def home(request):
    if request.method == "POST":
        url = request.POST.get("mediaUrl")

        download_folder = settings.MEDIA_ROOT

        if not os.path.exists(download_folder):
            os.makedirs(download_folder)

        ydl_opts = {
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'format': 'best',
            'quiet': False,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        # Make sure file exists before returning
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True)
        else:
            return render(request, "index.html", {
                "error": "Download failed."
            })

    return render(request, "index.html")