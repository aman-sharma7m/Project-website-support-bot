import streamlit as st
import os 
import time



st.set_page_config(page_title='Support chatbot for excelcult')
st.header('AI assistance for the website 😎😎')


#session states
if 'hug_key' not in st.session_state:
  st.session_state['hug_key']=''
if 'pine_key' not in st.session_state:
  st.session_state['pine_key']=''


#side menu
st.sidebar.header('😎🔑')
hug_key=st.sidebar.text_input('Enter the input hugging_face api key:',type='password')
pine_key=st.sidebar.text_input('Enter the pinecone api key: ',type='password')
submit= st.sidebar.button('Submit')

if submit:
  if pine_key!='' and hug_key!='':
    st.sidebar.success('👍 Keys Success!')
    st.session_state['hug_key']=hug_key
    st.session_state['pine_key']=pine_key
    with st.spinner('Wait for it...'):
      #scrape the data and get it 
      st.sidebar.write('🌍 scraping the data!!!! (1 of 4)')
      #chunk it 
      st.sidebar.write('🪓 Splitting scraped data!!! (2 of 4)')
      #get_embeddings
      time.sleep(5)
      st.sidebar.write('📃 Generating embeddings (3 of 4)')
      #create index and push the data-embedding to index
      st.sidebar.write('🏬 Storing the data embeddings (4 of 4)')
    #done
    st.sidebar.success('👉 Proceed to enter the query >>>>>>')

  else:
    st.sidebar.error('Error! Please enter the actual keys')


#input the query
query=st.text_input('Enter the organization name or role looking for:')

#input how many links required 
nlinks=st.slider('Select the no of rows:',1,10)

#search button 
search_b=st.button('Search')

if search_b:
  if st.session_state['pine_key']!='' and st.session_state['hug_key']!='':
    st.success('Generating the result')
    st.write(query)
    st.write(nlinks)
    st.subheader('Answers:',divider='rainbow')
    #retreival of documents

    #structured output
    
    
  else:
    st.error('Invalid keys')