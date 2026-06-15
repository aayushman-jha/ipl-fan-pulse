# 🏏 IPL Fan Pulse
 
A live IPL fan voting app where cricket fans can vote for their favourite team and see real-time results backed by a real SQL database.
 
🔗 **Live App:** [ipl-fan-pulse.streamlit.app](https://ipl-fan-pulse.streamlit.app/)
 
---
 
## What it does
 
- Vote for your favourite IPL team from all 10 franchises
- One vote per session — no spam voting
- Live vote counts updated in real time
- Results displayed as a sorted leaderboard
- Data seeded with realistic fan distributions so the app feels live from day one
---
 
## Tech Stack
 
| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Frontend and deployment |
| SQLite | Persistent vote storage |
| Pandas | Data handling for leaderboard display |
 
---
 
## What I learned building this
 
- Building interactive multi-column layouts in Streamlit
- Connecting SQLite database to a live web app
- Using `session_state` to prevent duplicate votes per session
- Data seeding — initializing a database with realistic starting data
- Deploying a Python app with a live URL on Streamlit Cloud
- Clean Git workflow with meaningful commit messages
---
 
## Run locally
 
```bash
git clone https://github.com/aayushman-jha/ipl-fan-pulse.git
cd ipl-fan-pulse
pip install -r requirements.txt
streamlit run streamlit_app.py
```
 
---
 
## Coming soon
 
- Player voting — vote for your favourite IPL player
- Fan Wall — see why other fans support their team
- Top 3 teams and players leaderboard with bar charts
