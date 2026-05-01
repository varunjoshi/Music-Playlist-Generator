from data import songs

print(" Music PLAYLIST GENERATOR ")
userchoice = input("Enter a mood (Hype,Chill,Vibey))")
userchoice = userchoice.strip().capitalize()
playlist = [s for s in songs if s['mood'] == userchoice]



print(f" Your {userchoice} Playlist : ")
for track in playlist :
     print(f"-{track['name']} by  {track['artist']} (energy :{track['energy']})")
