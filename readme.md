# Project Support-Chatbot-for-Excelcult

## Introduction

In this code, we will be implementing a support chatbot for the website Excelcult. The chatbot will provide AI assistance to users by answering their queries related to the organization or specific roles they are looking for.

## Installation & create environment

Clone the project

```bash
  git clone link_to_copy
```

Go to the project directory

```bash
  cd proj_dir
```

Create the enviroment

```bash
  conda create --prefix ./lang_env
  conda activate {path}/lang_env
  python -m ipykernel install --user --name=lang_env
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  streamlit run app.py
```

## Code Explanation

Streamlit: Streamlit is a Python library used for building interactive web applications. It allows developers to create user-friendly interfaces for their machine learning models or data analysis tools.

Session States: Session states are used to store and manage data across different sessions or interactions with the web application. In this code, we use session states to store the API keys and the embeddings generated during the scraping and indexing process.

Hugging Face API: Hugging Face is a popular platform for natural language processing (NLP) models and datasets. We use the Hugging Face API to generate embeddings for the scraped data and retrieve similar documents based on user queries.

Pinecone API: Pinecone is a vector database service that allows efficient storage and retrieval of high-dimensional embeddings. We use the Pinecone API to store the data embeddings and perform similarity searches.

The code is structured into several functions, each responsible for a specific task:

load_documents(): Loads documents from a specified web path using the SitemapLoader class.
chunking(docs): Splits the loaded documents into smaller chunks using the RecursiveCharacterTextSplitter class.
get_embeddings(api_key): Generates embeddings for each chunk of text using the SentenceTransformerEmbeddings class.
store_embeddings(chunk_data, embeddings, pine_key): Creates a new index and stores the embeddings of the chunked documents using the Pinecone class.
retrieve_similar_docs(embeddings, query, k): Retrieves similar documents based on a given query using the Pinecone class.

### Detailed Explanation:

Importing Libraries: We import the necessary libraries, including Streamlit, os, time, and a custom utility module called "utils".

Setting Page Configuration: We set the page title and display a header for the web application.

Session States: We check if the session states for the Hugging Face API key, Pinecone API key, and embeddings exist. If not, we initialize them.

Side Menu: We create a sidebar menu where the user can enter their Hugging Face API key and Pinecone API key. Upon clicking the "Submit" button, the keys are stored in the session states. If both keys are provided, the data scraping, chunking, embedding generation, and data storage processes are executed.

User Input: We provide an input field where the user can enter their query (organization name or role) and select the number of rows (links) they want to retrieve.

Search Button: Upon clicking the "Search" button, the code checks if the API keys are valid. If so, it retrieves similar documents based on the user's query and displays the results.

Document Loading: The load_documents() function uses the SitemapLoader class from the langchain.document_loaders.sitemap module to load documents from a specified web path.
Document Chunking: The chunking() function uses the RecursiveCharacterTextSplitter class from the langchain.text_splitter module to split the loaded documents into smaller chunks based on a specified chunk size and overlap.
Document Embeddings: The get_embeddings() function uses the SentenceTransformerEmbeddings class from the langchain.embeddings.sentence_transformer module to generate embeddings for each chunk of text. It requires an API key from Hugging Face's model hub to access the pre-trained models.
Vector Store: The store_embeddings() function uses the Pinecone class from the langchain.vectorstores module to create a new index and store the embeddings of the chunked documents. It requires an API key from Pinecone to access the vector store service.
Document Retrieval: The retrieve_similar_docs() function retrieves similar documents based on a given query. It uses the Pinecone class to access the existing index and perform a similarity search.

## AI Explaination:

This code is a Python script that performs various operations related to document loading, text chunking, embeddings, and similarity search.

The code begins by importing the necessary modules and packages. It imports the SitemapLoader class from the langchain.document_loaders.sitemap module, the nest_asyncio module, the constants module, the os module, the RecursiveCharacterTextSplitter class from the langchain.text_splitter module, the SentenceTransformerEmbeddings class from the langchain.embeddings.sentence_transformer module, and the Pinecone class from the langchain.vectorstores module. It also imports the Pinecone class from the pinecone module and the PodSpec class from the pinecone module.

The code then defines a function called load_documents(). This function applies the nest_asyncio module to enable asyncio event loops in Jupyter notebooks or IPython. It creates an instance of the SitemapLoader class with the web path specified in the constants module. It then calls the load() method of the SitemapLoader instance to load the documents and returns them.

The code also defines a function called chunking(docs). This function creates an instance of the RecursiveCharacterTextSplitter class with the chunk size and overlap specified in the constants module. It then calls the split_documents() method of the RecursiveCharacterTextSplitter instance to split the documents into chunks and returns the chunked text.

The code further defines a function called get_embeddings(api_key). This function sets the HUGGINGFACEHUB_API_KEY environment variable to the specified API key. It creates an instance of the SentenceTransformerEmbeddings class with the model name specified. It then returns the embeddings.

The code also defines a function called store_embeddings(chunk_data, embeddings, pine_key). This function sets the PINECONE_API_KEY environment variable to the specified Pinecone API key. It gets the dimension of the sentence embeddings from the embeddings object. It creates a new Pinecone instance with the specified API key. It then iterates over the existing indexes and deletes them if they exist. After that, it creates a new index with the specified name, dimension, metric, and environment. Finally, it uploads the documents' embeddings to the index using the from_documents() method of the Pinecone instance.

The code further defines a function called retrieve_similar_docs(embeddings, query, k). This function retrieves the index name from the constants module. It creates an instance of the Pinecone class with the existing index name and the embeddings object. It then performs a similarity search using the similarity_search() method of the Pinecone instance with the specified query and number of results. Finally, it returns the retrieved documents.

Overall, this code provides functions for loading documents, chunking text, getting embeddings, storing embeddings in a Pinecone index, and retrieving similar documents based on a query.

## libraries

```
from langchain.document_loaders.sitemap import SitemapLoader
import nest_asyncio
import constants
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Pinecone
from pinecone import Pinecone as pc ,PodSpec
import streamlit as st
```

## Conclusion

In this code, we have implemented a support chatbot for the Excelcult website using Streamlit, Hugging Face API, and Pinecone API. The chatbot allows users to enter their queries and retrieves similar documents based on the provided query. This AI assistance feature enhances the user experience and provides quick and relevant information to the users.
