from pytubefix import YouTube
from pytubefix.cli import on_progress

url = 'https://youtu.be/NDsO1LT_0lw?si=okHrvl99uWuN_ccA'
yt = YouTube(
        url,
        on_progress_callback=on_progress,
        on_complete_callback=on_progress,
        use_oauth=False,
        allow_oauth_cache=True
    )
# print(yt.age_check)
# print(yt.age_restricted)
# print(yt.author)
# print(yt.caption_tracks)
# print(yt.captions)
# print(yt.channel_url)
# print(yt.channel_id)
# print(yt.description)
# print(yt.embed_url)
# print(yt._vid_details)
# print(yt._vid_info)
# print(yt.video_id)
# print(yt.views)
# print(yt.visitor_data)
# print(yt.vid_info)
# print(yt.title)
# print(yt.signature_timestamp)
# print(yt.publish_date)
# print(yt.rating)
video = yt.streams.get_highest_resolution()
video.download()
