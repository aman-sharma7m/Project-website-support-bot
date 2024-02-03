import streamlit as st
import os 



st.set_page_config(page_title='Support chatbot for excelcult')
st.header('AI assistance for the website')


#side menu
st.sidebar.header('😎🔑')
hug_key=st.sidebar.text_input('Enter the input hugging_face api key:',type='password')
pine_key=st.sidebar.text_input('Enter the pinecone api key: ',type='password')
submit= st.sidebar.button('Submit')

if submit:
  if pine_key!='' and hug_key!='':
    st.sidebar.success('Got the keys! proceed')
    #input the query
    query=st.text_input('Enter the organization name or role looking for:')

    #input how many links required 
    nlinks=st.slider('Select the no of rows:',1,10)

    #search button 
    search_b=st.button('Search')

    if search_b:
      st.success('Generating the result')
      st.subheader('Answers:',divider='rainbow')
      st.write(query)
      st.write(nlinks)
  else:
    st.sidebar.error('Please enter the actual keys')