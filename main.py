import random
from data import music_library

# Display main menu
def show_menu():
    print("\n========================================")
    print("    MUSIC PLAYLIST GENERATOR")
    print("========================================")
    print("1. Playlist by Mood")
    print("2. Playlist by Genre")
    print("3. Random Playlist")
    print("4. Exit")
    print("========================================")

# Show playlist
def show_playlist(songs):
    print("\n--- YOUR PLAYLIST ---")
    for i in range(len(songs)):
        print(str(i+1) + ". " + songs[i]['title'] + " - " + songs[i]['artist'])
    print("Total: " + str(len(songs)) + " songs\n")

# generate playlist by mood
def get_by_mood():
    print("\nMoods: Calm, Energetic, Romantic, Spiritual, Devotional")
    mood = input("Enter mood: ").capitalize()
    
    result = []
    for song in music_library:
        if song['mood'] == mood:
            result.append(song)
    
    if len(result) > 10:
        result = result[:10]
    
    return result

# generate playlist by genre
def get_by_genre():
    print("\nGenres: Bollywood, Pop, Lo-fi, Devotional, Indian Classical")
    genre = input("Enter genre: ")
    
    result = []
    for song in music_library:
        if genre.lower() in song['genre'].lower():
            result.append(song)
    
    if len(result) > 10:
        result = result[:10]
    
    return result

# generate random playlist
def get_random():
    result = []
    for i in range(10):
        song = music_library[random.randint(0, len(music_library)-1)]
        result.append(song)
    return result


playlist = []

while True:
    show_menu()
    choice = input("Choose option: ")
    
    if choice == '1':
        playlist = get_by_mood()
        if len(playlist) > 0:
            show_playlist(playlist)
        else:
            print("No songs found!")
    
    elif choice == '2':
        playlist = get_by_genre()
        if len(playlist) > 0:
            show_playlist(playlist)
        else:
            print("No songs found!")
    
    elif choice == '3':
        playlist = get_random()
        show_playlist(playlist)
    
    elif choice == '4':
        print("\nThank You for using Music Playlist Generator!")
        break
    
    else:
        print("Invalid choice!")
