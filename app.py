import streamlit as st
import os 
import time
from utils import *


st.set_page_config(page_title='Support chatbot for excelcult')
st.header('AI assistance for the website 😎😎')


#session states
if 'hug_key' not in st.session_state:
  st.session_state['hug_key']=''
if 'pine_key' not in st.session_state:
  st.session_state['pine_key']=''
if 'embed' not in st.session_state:
  st.session_state['embed']=None


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
      docs=load_documents()
      print(f'Scraped docs-------{len(docs)}')

      #chunk it 
      st.sidebar.write('🪓 Splitting scraped data!!! (2 of 4)')
      chunk_data=chunking(docs)
      print(f'chunked docs-------{len(chunk_data)}')

      #get_embeddings
      st.sidebar.write('📃 Generating embeddings (3 of 4)')
      embeddings=get_embeddings(st.session_state['hug_key'])
      dim=embeddings.client.get_sentence_embedding_dimension()
      st.session_state['embed']=embeddings
      print(f'gen embeddings of dim-------{dim}')

      #create index and push the data-embedding to index
      st.sidebar.write('🏬 Storing the data embeddings (4 of 4)')
      store_embeddings(chunk_data,embeddings,st.session_state['pine_key'])
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
    st.subheader('Answers:',divider='rainbow')
    #get embeddings
    # embeddings=get_embeddings(st.session_state['hug_key'])
    #retreival of documents
    ret_docs=retrieve_similar_docs(st.session_state['embed'],query,nlinks)
    #structured output
    for i in ret_docs:
      st.write(i.metadata['loc'])
      st.write(i.page_content.split('\n')[0])
  else:
    st.error('Invalid keys')