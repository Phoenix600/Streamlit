import streamlit as st 


# This is how you import the image in streamlit 

st.write("# Importing Image ")
st.write('#### Path : Components/money.png')
st.image("Components/money.jpg",caption="No one cares how you feel, its all about making dollar bills",width=200)
st.video("Components/money.mp4")
st.audio("Components/SteveJobs.mp3",start_time=134)

