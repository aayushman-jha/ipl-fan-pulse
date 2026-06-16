import streamlit as st
import sqlite3
import pandas as pd

@st.cache_resource
def get_connection():
    return sqlite3.connect("votes.db", check_same_thread=False)

conn = get_connection()
cursor = conn.cursor()
#create table

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS team_votes (
    team_name TEXT PRIMARY KEY,
    vote_count INTEGER DEFAULT 0
    )
"""
)
conn.commit()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS player_votes (
    player_name TEXT PRIMARY KEY,
    vote_count INTEGER DEFAULT 0
    )
"""
)
conn.commit()

#Intitialize vote count

teams = {
    "rcb": 211,
    "csk": 198,
    "mi": 210,
    "kkr": 120,
    "gt": 89,
    "rr": 134,
    "lsg": 76,
    "dc": 92,
    "pbks": 103,
    "srh": 118
}

players = {

    # RCB 211
    "Virat Kohli": 127,
    "Rajat Patidar": 84,

    # CSK 198
    "MS Dhoni": 119,
    "Ravindra Jadeja": 79,

    # MI 210
    "Rohit Sharma": 126,
    "Jasprit Bumrah": 84,

    # KKR 120
    "Sunil Narine": 72,
    "Andre Russell": 48,

    # GT 89
    "Shubman Gill": 53,
    "Rashid Khan": 36,

    # RR 134
    "Sanju Samson": 80,
    "Yashasvi Jaiswal": 54,

    # LSG 76
    "KL Rahul": 46,
    "Nicholas Pooran": 30,

    # DC 92
    "Rishabh Pant": 55,
    "Axar Patel": 37,

    # PBKS 103
    "Arshdeep Singh": 62,
    "Shashank Singh": 41,

    # SRH 118
    "Travis Head": 71,
    "Abhishek Sharma": 47
}

for team,vote in teams.items():
    cursor.execute(
        "INSERT OR IGNORE INTO team_votes (team_name, vote_count) VALUES (?,?)",(team,vote)
    )
conn.commit()

for player,vote in players.items():
    cursor.execute(
        "INSERT OR IGNORE INTO player_votes (player_name, vote_count) VALUES (?,?)",(player,vote)
    )
conn.commit()

if "voted" not in st.session_state:
    st.session_state.voted = False
    
if "playerVoted" not in st.session_state:
    st.session_state.playerVoted = False
    
st.title("IPL Fan Pulse :cricket: :heart_eyes:",)
st.subheader("Vote for your Fav Team and Player :trophy: ",divider=True,text_alignment="center")

col1,col2,col3 = st.columns(3)

with col1:

    st.header("Sunrisers Hyderabad")
    st.image("pictures/hyd.png",width=100)
    vote_srh = st.button("Vote SRH") 

    st.header("Gujrat Titans")
    st.image("pictures/gt.png",width=100)
    vote_gt = st.button("Vote GT")

    st.header("Punjab Kings")
    st.image("pictures/pun.png",width=100)
    vote_pbks = st.button("Vote PBKS")

    st.header("Lucknow Super Giants")
    st.image("pictures/lsg.png", width=100)
    vote_lsg = st.button("Vote LSG")

with col2:

    st.header("Chennai Super Kings")
    st.image("pictures/csk.png",width=100)
    vote_csk = st.button("Vote CSK")

    st.header("Royal Challengers Bangalore")
    st.image("pictures/rcb.png",width=100)
    vote_rcb = st.button("Vote RCB")

    st.header("Mumbai Indians")
    st.image("pictures/mi.png",width=100)
    vote_mi = st.button("Vote MI")

with col3:
    st.header("Kolkata Knight Riders")
    st.image("pictures/kkr.png", width=100)
    vote_kkr = st.button("Vote KKR")


    st.header("Rajasthan Royals")
    st.image("pictures/rr.png", width=100)
    vote_rr = st.button("Vote RR")


    st.header("Delhi Capitals")
    st.image("pictures/dc.jpg", width=100)
    vote_dc = st.button("Vote DC")


def cast_vote(team):
    if not st.session_state.voted:
        cursor.execute(
            """
            UPDATE team_votes 
            SET vote_count = vote_count + 1 
            WHERE team_name = ? 

            """ , (team,)
        )
        conn.commit()

        st.session_state.voted = True
        st.success(f"Vote Recorded :smile: : {team}")
    else:
        st.warning("Already Voted")

vote_buttons = {
    "srh": vote_srh,
    "csk": vote_csk,
    "mi": vote_mi,
    "kkr": vote_kkr,
    "gt": vote_gt,
    "rr": vote_rr,
    "pbks": vote_pbks,
    "lsg": vote_lsg,
    "rcb": vote_rcb,
    "dc": vote_dc
}

for team, clicked in vote_buttons.items():
    if clicked:
        cast_vote(team)

fav_player = st.selectbox("Tell me whose your fav player is ?",players.keys())
player_voted = st.button("Vote Player")



def cast_playervote(player):
    if not st.session_state.playerVoted:
        cursor.execute(
            """
            UPDATE  player_votes 
            SET vote_count = vote_count + 1 
            WHERE player_name = ? 

            """ , (player,)
        )
        conn.commit()

        st.session_state.playerVoted = True
        st.success(f"Vote Recorded :smile: : {player}")
        
    else:
        st.warning("Already Voted")

if player_voted:
    cast_playervote(fav_player)

st.markdown("### 🏆 Live Fan Poll Results")

cursor.execute(
    """
    SELECT team_name,vote_count FROM team_votes
    ORDER BY vote_count DESC
    """
    )
result = cursor.fetchall()
team_df = pd.DataFrame(result, columns=["Team","Votes"])
st.markdown("### :medal_sports: Teams")
st.dataframe(team_df,hide_index=True)

cursor.execute(
    """
    SELECT player_name,vote_count FROM player_votes
    ORDER BY vote_count DESC
    """
    )
result = cursor.fetchall()
player_df = pd.DataFrame(result, columns=["Player","Votes"])
st.markdown("### :medal_sports: Players")
st.dataframe(player_df,hide_index=True)



