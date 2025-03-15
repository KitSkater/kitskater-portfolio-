import random

# Road trip song library
songs = {
    "Classic Rock": ["Born to Be Wild", "Sweet Home Alabama", "Life Is a Highway", "Take It Easy", "Go Your Own Way"],
    "Upbeat": ["Shut Up and Drive", "On Top of the World", "I'm Gonna Be (500 Miles)", "Send Me on My Way", "Uptown Funk"],
    "Chill": ["Riptide", "Slow Hands", "Banana Pancakes", "Come Away With Me", "Holocene"],
    "Hip-Hop": ["Lose Yourself", "POWER", "Sicko Mode", "HUMBLE.", "Wild for the Night"],
    "Country": ["Cruise", "Wagon Wheel", "Drunk on a Plane", "Take Me Home, Country Roads", "American Kids"],
    "Pop" : ["Dance Monkey", "Blinding Lights", "Shape of You", "Don't Start Now", "Watermelon Sugar"],
    "EDM" : ["Wake Me Up", "The Nights", "Titanium", "Closer", "Don't Let Me Down"], 
    "Vocaloid" : ["World is Mine", "The Vampire", "Rolling Girl"]
}

def generate_playlist(num_songs=5, genre=None):
    """Generates a random road trip playlist."""
    selected_songs = []
    
    if genre and genre in songs:
        selected_songs = random.sample(songs[genre], min(num_songs, len(songs[genre])))
    else:
        all_songs = [song for genre_songs in songs.values() for song in genre_songs]
        selected_songs = random.sample(all_songs, min(num_songs, len(all_songs)))

    return selected_songs

# User input
num_songs = int(input("How many songs do you want in your playlist? "))
genre = input("Choose a genre (or press Enter for random mix): ")

# Generate and display playlist
playlist = generate_playlist(num_songs, genre if genre in songs else None)
print("\n🎵 Your Road Trip Playlist 🎵")
for i, song in enumerate(playlist, 1):
    print(f"{i}. {song}")
