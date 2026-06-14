import streamlit as st

st.title("IPL Fan Pulse")
st.subheader("Vote for your Fav Team and Player")

col1,col2,col3 = st.columns(3)
col4,col5,col6 = st.columns(3)

with col1:

    st.header("Sunrisers Hyderabad")
    st.image("pictures/hyd.png",width=200)
    vote_hyd = st.button("Vote SRH") 
with col2:
    st.header("Royal Challengers Bangalore")
    st.image("pictures/rcb.png",width=200)
    vote_rcb = st.button("Vote RCB")
with col3:
    st.header("Chennai Super Kings")
    st.image("pictures/csk.png",width=200)
    vote_csk = st.button("Vote CSK")
with col4:
    st.header("Gujrat Titans")
    st.image("pictures/gt.png",width=200)
    vote_gt = st.button("Vote GT")
with col5:
    st.header("Mumbai Indians")
    st.image("pictures/mi.png",width=200)
    vote_mi = st.button("Vote MI")
with col6:
    st.header("Punjab Kings")
    st.image("pictures/pun.png",width=150)
    vote_pbks = st.button("Vote PBKS")
col7,col8,col9,col10 = st.columns(4)

with col7:
    st.header("Kolkata Knight Riders")
    st.image("pictures/kkr.png", width=200)
    vote_kkr = st.button("Vote KKR")

with col8:
    st.header("Rajasthan Royals")
    st.image("pictures/rr.png", width=200)
    vote_rr = st.button("Vote RR")

with col9:
    st.header("Lucknow Super Giants")
    st.image("pictures/lsg.png", width=200)
    vote_lsg = st.button("Vote LSG")

with col10:
    st.header("Delhi Capitals")
    st.image("pictures/dc.jpg", width=200)
    vote_dc = st.button("Vote DC")
