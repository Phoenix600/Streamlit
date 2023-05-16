import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError


st.markdown("# Mapping Demo")
st.sidebar.header("Mapping Demo")
st.write("""## Your Posts Will Be Displayed Here""")