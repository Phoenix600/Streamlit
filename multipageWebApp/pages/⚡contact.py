import streamlit as st


contact_form = """
<style>

    button{
        padding : 5px 10px;
        border-radius : 5px;
        background : #ffd500;
    }
    button:hover{
        background : #363574;
        color : white;
    }
</style>
<form action="https://formsubmit.co/pranayramteke613@gmail.com" method="POST">
    <h3>📰 Join News Letter </h3>
     <input type="text" name="name" required> <br><br>
     <input type="email" name="email" required> <br><br>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form,unsafe_allow_html=True)
st.write("""## Contact Here""")

