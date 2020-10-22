# youtube-dl-playlist-subtitles
A small script to download subtitles from every video in a YouTube channel, the fast way.

The script extracts the JSON of the flattened playlist and enumerates over it to extract video ids, instead of doing an API call for each video individually. This approach is way faster for channels with lots of videos.
