import streamlit as st 
import mysql.connector
import streamlit.components.v1 as components
from components import productCard

# Connection String For The Data Base 
mydb = mysql.connector.connect(
    host = "localhost",
    user = "pranay",
     password = "root"
)

# def intro():
#     st.write("# Welcome the Rewire Mindset")
#     st.sidebar.success("Home")
#     add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# Creating the entery point page for the application 


# Setting the page configurations 
st.set_page_config(
    page_title="rewiremindset",
    page_icon="🧠"
)

# Adding the Content for the page 
st.write("# Welcome to Rewire Mindset 🧠")

st.markdown("## Become The Part of the Community Where Leader Like You Come Together and Inspire The World")
st.button(label="Get Started")

st.markdown(
    """
    <style>
    .stApp{
          {
              background-image : url("assets/Media.jpg");
              background-size : cover;
          }  
        }
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
### Start Dancing With Your Fears 
- A easy and simple path to the overcomming your fears
- Listen it on [spofity](https://open.spotify.com/)
- Watch it on [YouTube](https://www.youtube.com/@mindsetofficial)
            """)