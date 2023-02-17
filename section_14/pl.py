playlist = {
    "title": "my playlist", 
    "owner": "f4shback", 
    "songs": [
        {"name": "Sing in the Rain", "order": 2, "duration": 3.24, "artist": ["Chrisophe", "Flavie"], "album": "Random Album"}, 
        {"name": "Let the Wind Flow", "order": 0, "duration": 5.26, "artist": ["Elle", "Lui"], "album": "Rain Wishes"},
        {"name": "Lava Will Burn", "order": 10, "duration": 4.47, "artist": ["Deatheater"], "album": "Environmental Disasters"}
    ]
}
pl_duration = 0
for song in playlist["songs"]:
    pl_duration += song["duration"]
print(round(pl_duration, 2))
