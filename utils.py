from langchain.document_loaders.sitemap import SitemapLoader
import nest_asyncio
import constants
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Pinecone
from pinecone import Pinecone as pc ,PodSpec


def load_documents():
  nest_asyncio.apply()
  site_loader=SitemapLoader(web_path=constants.site)
  docs=site_loader.load()
  return docs

def chunking(docs):
  text_split=RecursiveCharacterTextSplitter(chunk_size=constants.chunk_size,chunk_overlap=constants.chunk_overlap,length_function=len)
  chunk_text=text_split.split_documents(docs)
  return chunk_text

def get_embeddings(api_key):
  os.environ['HUGGINGFACEHUB_API_KEY']=api_key
  embeddings=SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-V2')
  return embeddings

def store_embeddings(chunk_data,embeddings,pine_key):
  os.environ['PINECONE_API_KEY']=pine_key
  index_name=constants.index_name
  dim=embeddings.client.get_sentence_embedding_dimension()

  # create new index and delete previous index if exist
  pc_config = pc(api_key=pine_key)

  for name in pc_config.list_indexes().names():
    try:
      pc_config.delete_index(name)
    except Exception as e:
      print('no index is there')

  pc_config.create_index(
          index_name,
          dimension=dim,  
          metric='dotproduct',
          spec=PodSpec(environment='gcp-starter')
      )
  
  # uploading the documents embedding
  Pinecone.from_documents(chunk_data,embeddings,index_name=index_name)



def retrieve_similar_docs(embeddings,query,k):
  index_name=constants.index_name
  index=Pinecone.from_existing_index(index_name,embeddings)
  ret_docs=index.similarity_search(query,k)
  return ret_docs

  