from pytubefix import YouTube
from pytubefix.cli import on_progress
import re

video_urls = [
    "https://www.youtube.com/watch?v=iZ3g7JdSjbw",
    "https://www.youtube.com/watch?v=uVAo7-4VKh4",
    "https://www.youtube.com/watch?v=d85818yUU60",
    "https://www.youtube.com/watch?v=7WUPTe39fMg",
    "https://www.youtube.com/watch?v=r8G6dxvBDmg",
    "https://www.youtube.com/watch?v=FPXjypbgFUA",
    "https://www.youtube.com/watch?v=w2DlMu8ZzHE",
    "https://www.youtube.com/watch?v=0_URFaZQXUU",
    "https://www.youtube.com/watch?v=4EbJWuq3PUo",
    "https://www.youtube.com/watch?v=t3cjesk9H-s",
    "https://www.youtube.com/watch?v=fAXaowWbsxI",
    "https://www.youtube.com/watch?v=g9Tnj90w1BE",
    "https://www.youtube.com/watch?v=LMHI2tXKeAY",
    "https://www.youtube.com/watch?v=i2HczDAJrYU",
    "https://www.youtube.com/watch?v=r2pvNu4sY6s",
    "https://www.youtube.com/watch?v=Q6Kd1oYaauc",
    "https://www.youtube.com/watch?v=ceyihXC6Ao8",
    "https://www.youtube.com/watch?v=-IOgQXf0z24",
    "https://www.youtube.com/watch?v=cYfXh2dD_cM",
    "https://www.youtube.com/watch?v=ZZouuAa_OtA",
    "https://www.youtube.com/watch?v=E8SyjD7PqxM",
    "https://www.youtube.com/watch?v=NZgmuPN8b7c",
    "https://www.youtube.com/watch?v=O6BxZsq6cVk",
    "https://www.youtube.com/watch?v=26FHuxnl54U",
    "https://www.youtube.com/watch?v=zqEQa1Qpa2c",
    "https://www.youtube.com/watch?v=Ci7WMxdbBxk",
    "https://www.youtube.com/watch?v=lG1tGGpqye0",
    "https://www.youtube.com/watch?v=ceyihXC6Ao8",
    "https://www.youtube.com/watch?v=-IOgQXf0z24",
    "https://www.youtube.com/watch?v=jf4rRlu8UZA",
    "https://www.youtube.com/watch?v=yFylYFkwB54",
    "https://www.youtube.com/watch?v=GcJvvYXJffw",
    "https://www.youtube.com/watch?v=Y6WYqnGOCKA",
    "https://www.youtube.com/watch?v=rhqRCAhfxxQ",
    "https://www.youtube.com/watch?v=wq-IQVNcSjk",
    "https://www.youtube.com/watch?v=UP2SX1aLJ60",
    "https://www.youtube.com/watch?v=8T_AUR8p-Sg",
    "https://www.youtube.com/watch?v=gIvJqwSMdJg",
    "https://www.youtube.com/watch?v=L8CFekze7co",
    "https://www.youtube.com/watch?v=wx676fYedZ0",
    "https://www.youtube.com/watch?v=vn__Qv0V2ts",
    "https://www.youtube.com/watch?v=5SrzgaTAyqo",
    "https://www.youtube.com/watch?v=3zOtLEeHygg",
    "https://www.youtube.com/watch?v=wGLTV8MgLlA",
    "https://www.youtube.com/watch?v=8xvHsh3MGvg",
    "https://www.youtube.com/watch?v=riPbSRxatJ4",
    "https://www.youtube.com/watch?v=vK5NsISFNsg",
    "https://www.youtube.com/watch?v=eemPT2WGGnM",
    "https://www.youtube.com/watch?v=OMmaW95gwAs",
    "https://www.youtube.com/watch?v=papVRQqtrgc",
    "https://www.youtube.com/watch?v=DSHy6wJ4e7k",
    "https://www.youtube.com/watch?v=LOfGJcVnvAk",
    "https://www.youtube.com/watch?v=TCWOwavqFrw",
    "https://www.youtube.com/watch?v=DmgQVJXhuLQ",
    "https://www.youtube.com/watch?v=iZ3g7JdSjbw",
    "https://www.youtube.com/watch?v=59fUtYYz7ZU",
    "https://www.youtube.com/watch?v=uDulBxDb7GM",
    "https://www.youtube.com/watch?v=eI4an8aSsgw"
]

# Set the download path
download_path = "D:\\Study Material\\D.M."

for i, url in enumerate(video_urls, start=1):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        # Select the highest-resolution stream
        video_stream = yt.streams.get_by_itag(22) or yt.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").desc().first()

        if not video_stream:
            print(f"Skipping {url}: No suitable video stream found.")
            continue

        # Remove invalid characters from filename
        file_name = re.sub(r'[\/:*?"<>|]', "_", f"lec{i}_{yt.title}.mp4")

        print(f"Downloading {file_name} ({video_stream.resolution})...")

        video_stream.download(output_path=download_path, filename=file_name)

        print(f"Download Completed: {file_name}\n")

    except Exception as e:
        print(f"Error downloading {url}: {e}\n")
