import streamlit as st 

# Getting Started With The Markdown functions 
st.markdown("**Hello**")
st.markdown("# This Markdown Heading")
st.markdown("## Heading-2")
st.markdown('### Heading-3')
st.markdown('#### Heading-4')
st.markdown('##### Heading-5')
st.markdown('###### Heading-6')

st.markdown('*This is italic text*')
st.markdown("**This is unordered list**")
st.markdown("""  
    - Item-01 
    - Item-02 
    - Item-03 
""")
st.markdown("# This is ordered list")
st.markdown(""" 
    1. Item-A 
    2. Item-B 
    3. Item-C 
""")


st.markdown("# This is how you can add links ")
st.markdown("[Google](www.sbjain.com)")
st.markdown("---")
st.caption("Hi I'm Caption")
st.latex(r"\begin{pmatrix}a&b\\c&d\end{pmatrix}") # Latex code  visit : Katex.org 

json = {
    "a" : "1,2,3,4,",
    "b" : "4,5,6,7",
}
st.json(json)

code = """
print("Print function in python ....")
printf("Print function in C")
console.log("Print function in javascript")
"""

st.code(code,language="c",line_numbers=True)



# Display code of the programming langauges in more elegant way 
codes = {
    "c" : """
    #include<stdio.h>
    struct Node{
    int vertex;
    int key;
    };
    int main()
    {
        return 0;
    }
    """,
    "python" : """
    print("Hello Root User")
    """,
    "js" : "console.log('Hello')"
}

st.code(codes['c'],language="c",line_numbers=True)
st.code(codes['python'],language="python",line_numbers=True)
st.code(codes['js'],language="js",line_numbers=True)

st.markdown("# You can also display images locally as well as from url ")
st.markdown("![this is a image conatiner](https://images.unsplash.com/photo-1682397125573-4f99630e5de0?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80)")

st.metric(label="Matrix",value="120 mps",delta="-1.4 mps")
