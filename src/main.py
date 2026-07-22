"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 

    profiles = {
        "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8},
        "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.35},
        "Deep Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
        "Conflicted Edge Case": {"genre": "pop", "mood": "sad", "energy": 0.9},
    }

    print(f"Loaded songs: {len(songs)}")
    for profile_name, user_prefs in profiles.items():
        print(f"\n=== {profile_name} ===")
        for position, (song, score, explanation) in enumerate(
            recommend_songs(user_prefs, songs, k=5), start=1
        ):
            print(f"{position}. {song['title']} by {song['artist']} - Score: {score:.2f}")
            print(f"   Because: {explanation}")


if __name__ == "__main__":
    main()
