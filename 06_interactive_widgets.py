import streamlit as st 

st.markdown("""
<style>
    .css-9s5bis.edgvbvh3{
        visibility : hidden;
    }

    .css-h5rgaw.egzxvld1{
        
        visibility : hidden;
    }
    }

</style>
""",unsafe_allow_html=True)



st.header("Check box in streamlit")
st.checkbox(label="MD",value=False)
st.checkbox(label="Quber",value=True)

st.header("This check uncheck this shit: ")
checkBox1 = st.checkbox(label="CheckBox",value=True)
if checkBox1 :
    st.write("#### True")
else :
    st.write("#### False")


def onCheckedMethod():
    print("You just checked the button")

st.markdown("# on_check propery : ")
checkBox2 = st.checkbox(label="Red Label",value=True,on_change=onCheckedMethod)

checkBox3 = st.checkbox(label="Blue Label",value=False,on_change=onCheckedMethod)