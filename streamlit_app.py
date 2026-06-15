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
    CREATE TABLE IF NOT EXISTS votes (
    team_name TEXT PRIMARY KEY,
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

for team,vote in teams.items():
    cursor.execute(
        "INSERT OR IGNORE INTO votes (team_name, vote_count) VALUES (?,?)",(team,vote)
    )
conn.commit()

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

if "voted" not in st.session_state:
    st.session_state.voted = False

def cast_vote(team):
    if not st.session_state.voted:
        cursor.execute(
            """
            UPDATE votes 
            SET vote_count = vote_count + 1 
            WHERE team_name = ? 

            """ , (team,)
        )
        conn.commit()

        st.session_state.voted = True
        st.success("Vote Recorded :smile:")
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


cursor.execute(
    """
    SELECT team_name,vote_count FROM votes
    ORDER BY vote_count DESC
    """
    )
result = cursor.fetchall()
df = pd.DataFrame(result, columns=["Team","Votes"])
st.markdown("### 🏆 Live Fan Poll Results")
st.dataframe(df,use_container_width=True)



