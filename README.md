# 🏏 IPL Fan Pulse

My first real project — a live IPL fan engagement app where users vote for their favourite team and player, leave a message on a live fan wall, and watch results update in real time, all backed by a persistent SQL database.

🔗 **Live App:** [ipl-fan-pulse.streamlit.app](https://ipl-fan-pulse.streamlit.app/)

---

## Why I built this

I wanted my first GitHub repo to be something original, not a tutorial clone. IPL is something every cricket fan in India has an opinion about, so a live voting app felt like a natural way to learn Streamlit and SQL together while building something people would actually want to use.

This was also my first time working with Streamlit's interactive widgets and connecting a real database to a deployed web app.

---

## What it does

- Vote for your favourite team out of all 10 IPL franchises
- Vote for your favourite player — unlocked only after voting for a team, to keep voting data consistent
- One vote per session for both team and player, enforced with session state
- Leave a message on the live Fan Wall, visible to everyone instantly
- Live leaderboards for both teams and players, sorted by vote count
- Bar chart for team votes and a donut chart for the top 5 most voted players
- Fan wall timestamps converted to IST so they read naturally for Indian users
- Database seeded with realistic starting vote distributions so the app feels alive from the very first visit

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend and deployment |
| SQLite | Persistent storage for votes and fan messages |
| Pandas | Querying results into clean, sortable tables |
| Plotly | Donut chart for player vote share |

---

## App structure and flow

The app runs as a single Streamlit script, top to bottom, on every interaction:

1. **Connect to the database** — `@st.cache_resource` opens one SQLite connection and reuses it across reruns instead of reconnecting every time.
2. **Set up tables** — Three tables are created if they don't already exist: `team_votes`, `player_votes`, and `fan_wall`.
3. **Seed starting data** — Each table is pre-filled with realistic vote counts and a few sample fan messages, using `INSERT OR IGNORE` so seeding only happens once and never overwrites real votes.
4. **Render the team grid** — 10 teams are laid out across 3 columns, each with a logo and a vote button.
5. **Handle the team vote** — A dictionary maps each button to its team code, looped through to call `cast_vote()`, which checks `session_state.voted` before updating the database, so a user can only vote once.
6. **Unlock player voting** — Only after `session_state.voted` is `True` does the player dropdown and vote button appear, using the same one-vote logic with `session_state.playerVoted`.
7. **Fan Wall input** — A text box and name field let anyone post a message, inserted into `fan_wall` with an auto-generated timestamp.
8. **Display live results** — The script queries all three tables fresh on every rerun, turns the results into Pandas DataFrames, and renders a team leaderboard with a bar chart, a player leaderboard with a Plotly donut chart, and the 10 most recent fan messages with timestamps converted to IST.

---

## How the project grew

This app didn't start this complete. It was built in stages, with each stage adding one new concept:

1. **Basic UI** — Just the team layout, images, and vote buttons. First time using Streamlit's columns and widgets to lay out an interactive page.
2. **UI polish** — Added emojis, section dividers, and headers to make the interface feel less like a plain form and more like a finished product.
3. **SQLite integration** — Connected a real database, created the votes table, and got persistence working for the first time.
4. **Session state** — Added logic so a single visitor could only vote once, instead of spamming the vote count.
5. **Player voting + Fan Wall** — Added a second and third table, introduced AUTOINCREMENT and timestamps, and learned to sequence two related actions (team vote unlocking player vote) using session state together.
6. **Visualization** — Added a bar chart and a Plotly donut chart, and learned to convert UTC timestamps to IST for a more natural reading experience.
7. **Bug fix** — Realized team and player votes weren't actually linked, and fixed the flow so player voting only unlocks after a team vote, keeping the data consistent.

---

## What I learned building this

- Using Streamlit's widgets and layout system (`columns`, `button`, `selectbox`, `text_input`) to build a working interactive app from scratch
- Structuring multiple related SQLite tables instead of one flat table
- Using `@st.cache_resource` to avoid reconnecting to the database on every rerun
- Writing parameterized SQL queries to avoid injection issues, instead of string formatting queries directly
- Using `session_state` to control sequential user flows, not just simple one-off flags
- Data seeding — initializing a database with realistic values so a new app doesn't look empty on first load
- Converting timestamps between timezones for a better user experience
- Visualizing the same data two different ways (bar chart vs donut chart) depending on what story it tells
- Writing clean Git commit messages that document a project's actual growth over time

---

## Run locally

```bash
git clone https://github.com/aayushman-jha/ipl-fan-pulse.git
cd ipl-fan-pulse
pip install -r requirements.txt
streamlit run streamlit_app.py
```
