playlist = {
    "title": "my playlist", 
    "owner": "f4shback", 
    "songs": [
        {"name": "sing in the rain", "order": 2, "duration": 3.24, "artist": ["chrisophe", "flavie"], "album": "random album"}, 
        {"name": "windflow", "order": 0, "duration": 5.26, "artist": ["elle", "lui"], "album": "rain wishes"}
    ]
}
pl_duration = 0
for song in playlist["songs"]:
    pl_duration += song["duration"]
print(pl_duration)
