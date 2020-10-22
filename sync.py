import os
from youtube_dl import YoutubeDL

playlist_url = 'https://www.youtube.com/c/MyChannel/videos' # change this to the channel
existing_video_subs = []

# to avoid downloading the existing subtitles
for filename in os.listdir('.'):
    if '.vtt' in filename:
        existing_video_subs.append( filename[-18:][0:11] ) # store only the video_id part of the filename

playlist_ydl = YoutubeDL({
    'ignoreerrors': True,
    'extract_flat': 'in_playlist',
    'dump_single_json': True,
    'quiet': False
})
    
subtitle_ydl = YoutubeDL({
    'ignoreerrors': True,
    'quiet': False,
    'skip_download': True,
    'writesubtitles': True, # include manual subtitles
    'writeautomaticsub': True, # include automatic subtitles
    'subtitleslangs': ['en'] # only English subtitles, you can remove this if you want all languages.
})
    
with subtitle_ydl:
    with playlist_ydl:
        playlist_dict = playlist_ydl.extract_info(playlist_url, download=False)
            
        for i, item in enumerate(playlist_dict['entries']):
            video_id = item['id']
            
            if video_id in existing_video_subs:
                print('video already exists, skipping: %s' % (video_id))
                continue
                
            subtitle_ydl.download(['https://www.youtube.com/watch?v=%s' % (video_id)])
