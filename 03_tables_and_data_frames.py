import pandas as pd 
import streamlit as st  

class PandasTable : 

    def __init__(self):

        # Table_table = pd.DataFrame
        Table = {
        "Name" : ["Pranay","Vedant","Vishal","Mayur","Tanvi","Parul"],
        "College" : ["SB JAIN","IHM BOMBAY","GCOE","IIT Patna","GMC","GH Raisoni"],
        "Age" : [20,21,22,21,20,20]
        }

        Table = pd.DataFrame(Table)
        st.table(Table)



OBJECT = PandasTable()
# OBJECT.init()

