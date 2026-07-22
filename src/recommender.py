import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the k songs with the highest preference scores."""
        return sorted(self.songs, key=lambda song: self._score(user, song), reverse=True)[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain which preferences contributed to a song's score."""
        reasons = []
        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match")
        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match")
        reasons.append(f"energy is {abs(song.energy - user.target_energy):.2f} from target")
        if user.likes_acoustic and song.acousticness >= 0.6:
            reasons.append("strong acoustic fit")
        elif not user.likes_acoustic and song.acousticness < 0.6:
            reasons.append("non-acoustic fit")
        return ", ".join(reasons)

    @staticmethod
    def _score(user: UserProfile, song: Song) -> float:
        """Calculate an internal compatibility score for one Song object."""
        score = 0.0
        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0
        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0
        score += max(0.0, 1.0 - abs(song.energy - user.target_energy))
        if user.likes_acoustic == (song.acousticness >= 0.6):
            score += 0.5
        return score

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from CSV and convert numeric fields to numbers."""
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            row["id"] = int(row["id"])
            row["tempo_bpm"] = int(row["tempo_bpm"])
            for field in ("energy", "valence", "danceability", "acousticness"):
                row[field] = float(row[field])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song and return both its score and human-readable reasons."""
    score = 0.0
    reasons = []

    if song["genre"].lower() == user_prefs["genre"].lower():
        score += 2.0
        reasons.append("genre match (+2.0)")
    if song["mood"].lower() == user_prefs["mood"].lower():
        score += 1.0
        reasons.append("mood match (+1.0)")

    energy_points = max(0.0, 1.0 - abs(song["energy"] - user_prefs["energy"]))
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")
    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song and return the top k in descending order."""
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        ranked.append((song, score, "; ".join(reasons)))
    return sorted(ranked, key=lambda result: result[1], reverse=True)[:k]
