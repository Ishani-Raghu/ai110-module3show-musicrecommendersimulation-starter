# 🎧 Model Card: VibeBridge 1.0

## 1. Model Name  

**VibeBridge 1.0**

---

## 2. Intended Use  

VibeBridge ranks songs for a listener using a favorite genre, favorite mood, and target energy level. It assumes the listener can summarize their current taste with these three preferences. It is a classroom simulation, not a production service or a tool for making important decisions.

---

## 3. How the Model Works  

Each song receives 2 points when its genre matches, 1 point when its mood matches, and up to 1 point based on how close its energy is to the user's target. A perfect energy match earns the full point, while a larger energy gap earns less. The model scores every song, sorts the results from highest to lowest, and returns the top five. Unlike the starter, this version loads typed CSV data, gives explanations, and performs real ranking.

---

## 4. Data  

The catalog contains 18 fictional songs. Eight songs were added to the original ten to include R&B, EDM, folk, hip-hop, and additional jazz, rock, pop, and ambient examples. Fields include title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The current scoring rule uses genre, mood, and energy, so it does not yet use all available fields. The catalog still cannot represent the full range of music, cultures, languages, or changing listener preferences.

---

## 5. Strengths  

The system works best when the catalog contains an exact genre and mood match. The Chill Lofi profile correctly ranks low-energy, chill lofi songs first. The Intense Rock profile also places intense, high-energy rock songs at the top. Its explanations make each ranking easy to understand.

---

## 6. Limitations and Bias 

The genre weight is twice the mood weight, so an exact genre match can outrank a song that better fits the user's mood. This can create a filter bubble by repeatedly recommending the same genre and limiting discovery. Some genres have only one song, while pop and lofi have several, giving some profiles more meaningful choices than others. The system also ignores listening history, lyrics, language, artist diversity, and the fact that a person's taste may change by situation. The conflicted pop-and-sad profile demonstrates this weakness because genre-matching pop songs can rank highly even when their happy or intense moods conflict with the requested sadness.

---

## 7. Evaluation  

I tested High-Energy Pop, Chill Lofi, Deep Intense Rock, and a conflicted edge case combining pop, sadness, and high energy. I checked whether exact matches appeared first and whether nearby-energy songs moved upward. High-Energy Pop favored Sunrise City, while Chill Lofi shifted strongly toward Library Rain and Midnight Coding because both genre and mood matched. Deep Intense Rock preferred Fire in the Static and Storm Runner because they matched both labels and were near the target energy. The edge case showed that the large genre weight can overcome a mood mismatch.

I also performed a weight-shift thought experiment by reducing genre from 2.0 to 1.0 and doubling energy similarity from 1.0 to 2.0. This would increase the influence of musical intensity and make cross-genre songs more competitive. It may improve discovery, but it can also make recommendations feel less connected to a user's stated favorite genre. The comparison showed that changing weights does not make results automatically better; it changes which definition of similarity the system prioritizes.

---

## 8. Future Work  

I would use valence, danceability, acousticness, and tempo in the score and let users control their importance. I would add listening feedback such as likes and skips so preferences can update over time. I would also add a diversity rule that limits repeated artists or genres in the top five.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how a few understandable rules can produce results that feel personalized. AI helped me brainstorm features, scoring rules, edge cases, and clear explanations, but I still had to check its math, verify data types, run tests, and decide whether its suggestions matched the project requirements. I was surprised that such a small algorithm could create convincing recommendations while also creating a filter bubble so easily. This changed how I think about music apps because every recommendation reflects choices about data, weights, and what the platform defines as similar. If I continued the project, I would add user feedback and compare multiple scoring modes.
