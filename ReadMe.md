# Streamlit 

## Methods 
1. title() : Method lets you set the title of the web page.
    - args : String 
2. subheader() Method lets you set the subTitle of the web page.
    - args : String  
3. button(): Method lets you add the Button on webPage 
    - args : label="String"
4. text() : Method lets you add the text data on the web app


## Markdown Manipulation With markdown() method 

- markdown() method lets you write the markdown text 
in your web application.

```python
import streamlit as st 
st.markdown("**Hello**")
st.markdown("# This Markdown Heading")
st.markdown("## Heading-2")
st.markdown('### Heading-3')
st.markdown('#### Heading-4')
st.markdown('##### Heading-5')
st.markdown('###### Heading-6')
st.markdown('*This is italic text*')
st.markdown("**This is unordered list**")

```

