import streamlit as st
from awslib import s3_contents
from linelib import simple_recorder 
##############################################
st.set_page_config(layout="wide")

tab1, tab2 = st.tabs(['Grabación','Revisión'])
with tab1:
    st.title('👩‍🏫 Colegio San Juan escriba digital 🤖')
    simple_recorder()
with tab2:
    st.header('Revisión)
    contents = s3_contents()  
    st.table(contents)
