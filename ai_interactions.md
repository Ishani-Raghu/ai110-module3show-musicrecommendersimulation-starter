# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->
# AI Interaction Log

## Understanding and design

**Prompt:** Explain the difference between collaborative filtering and content-based filtering for music recommendations. Identify data such as likes, skips, playlists, genre, mood, tempo, and energy, then suggest a simple classroom scoring rule.

**Summary:** The AI explained that collaborative filtering learns from patterns across users, while content-based filtering compares item attributes with one user's preferences. It suggested exact-match points plus distance-based numerical similarity.

**My verification:** I chose content-based filtering because the starter dataset contains song attributes but no real listening histories. I checked that the scoring weights add logically and that energy rewards closeness instead of simply rewarding high energy.

## Dataset expansion

**Prompt:** Add eight fictional songs using the existing CSV headers. Include diverse genres and moods, keep energy, valence, danceability, and acousticness between 0 and 1, and use realistic tempos.

**Summary:** The AI proposed R&B, EDM, folk, hip-hop, jazz, rock, ambient, and pop additions.

**My verification:** I kept the exact header order, checked every row had ten fields, confirmed numeric ranges, and loaded the final file through Python's CSV module.

## Implementation

**Prompt:** Implement `load_songs`, `score_song`, and `recommend_songs`. Convert numeric CSV values, award 2 points for genre, 1 for mood, and up to 1 for energy closeness. Return a score and reasons, then rank the top k songs.

**Summary:** The AI helped produce modular loading, scoring, explanation, and sorting logic.

**My verification:** I ran `pytest` and `python -m src.main`. I also checked that `sorted()` returns a new ranked list without changing the original catalog, unlike `.sort()`, which changes a list in place.

## Evaluation and bias

**Prompt:** Suggest three distinct profiles and one adversarial profile. Identify filter bubbles or biases and describe a weight-shift experiment.

**Summary:** The AI suggested pop/happy, lofi/chill, rock/intense, and a conflicting pop/sad profile. It identified genre dominance and catalog imbalance as risks.

**My verification:** I compared the actual top-five outputs. The results confirmed that exact genre matches receive a strong advantage even when mood conflicts, so I documented that limitation in the Model Card.
