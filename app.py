from dotenv import load_dotenv
load_dotenv()

import os

from llama_index.core import VectorStoreIndex, Settings

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.sambanovasystems import SambaNovaCloud
from llama_index.llms.cohere import Cohere
from llama_index.vector_stores.astra_db import AstraDBVectorStore

import streamlit as st

st.set_page_config(
    page_title="Work-Permit Chatbot",
    page_icon=":robot_face:"
)

with st.expander("Disclaimer", icon="ℹ️"):
    st.markdown(''' 
        The responses provided by this 🤖 chatbot are for informational purposes only and are based on the content scraped from the IRCC website. While the chatbot strives to provide accurate and helpful answers, it may occasionally provide incorrect or outdated information. 🌐 For the most reliable and up-to-date details regarding work permits and immigration policies, please refer directly to the official 🔗 [IRCC website](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/permit.html). ❗ The use of this chatbot does not replace professional or official advice from authorized sources.
    ''')

st.title("Work-Permit Chabot")


@st.cache_resource(show_spinner=False)
def init():
    embed_model_name = "BAAI/bge-large-en-v1.5"
    embed_model = HuggingFaceEmbedding(model_name=embed_model_name)
    Settings.embed_model = embed_model

    # llm = Cohere(
    #     model="command-r-plus",
    #     api_key=os.getenv("COHERE_API")
    # )

    llm = SambaNovaCloud(
        model="Meta-Llama-3.1-70B-Instruct",
        context_window=100000,
        max_tokens=1024,
        temperature=0.3,
    )
    
    Settings.llm = llm

    astra_db_store = AstraDBVectorStore(
        token=os.getenv('ASTRA_DB_APPLICATION_TOKEN'),
        api_endpoint=os.getenv('ASTRA_DB_API_ENDPOINT'),
        collection_name="ircc_wp_vector_emb",
        embedding_dimension=1024
    )

    index = VectorStoreIndex.from_vector_store(vector_store=astra_db_store)

    system_template = (
        "You are an AI assistant for a government agency."
        "\nYour role is to provide clear, concise, empathetic, and accurate responses to user queries, adapting your language and tone to the context and nature of the query."
        "\nFormat your response as a direct and tailored answer, addressing the user's query and providing relevant context and essential information only."
        "\nInclude RELEVANT sources in the following format: '[Your response here, demonstrating understanding and sensitivity to the user's context and situation] Sources: 1. [URL](URL) 2. [URL](URL) Remember to respect confidentiality and keep your response well-structured, easy to understand, and empathetic.'"
        "\nMake the response concise."
    )

    chat_engine = index.as_chat_engine(
        similarity_top_k=5,
        chat_mode="condense_plus_context",
        system_prompt=system_template,
        verbose=True,
        streaming=True
    )

    return chat_engine


if "chat_engine" not in st.session_state:
    st.session_state.chat_engine = init()

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "Assistant",
        "content": "How can I help you today?"
    }]

# Take prompt from user
if prompt := st.chat_input("Write your query here"):
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })
    

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])

if st.session_state.messages[-1]['role'] == 'user' and prompt != None:
    print("Prompt: ", prompt)
    with st.chat_message("assistant"):
        query = st.session_state.messages[-1]['content']
        
        response = st.session_state.chat_engine.stream_chat(query)

        st.write_stream(response.response_gen)
        st.session_state.messages.append({
            "role": "assistant",
            "content": response.response
        })