# IRCC Work-Permit Chatbot

## Overview
The **IRCC Work-Permit Chatbot** is an AI-driven solution designed to assist users with their work-permit-related questions. The chatbot leverages advanced technologies to provide accurate and contextually relevant responses by combining web scraping, vector search, and a powerful large language model. It aims to enhance user experience by offering reliable information while integrating an interactive frontend.

## Key Features
- **Data Scraping**: IRCC webpages related to work permits were scraped (with proper permissions) to extract valuable information.
- **Vector Store**: The scraped data was converted into embeddings and stored in **DataStax AstraDB's vector store** for efficient retrieval.
- **LLM Integration**: The chatbot uses **SambaNova's large language model (LLM)** for generating contextually accurate answers.
- **RAG Architecture**: A **Retrieval-Augmented Generation (RAG)** approach is implemented using **llama-index** to fetch the most relevant documents.
- **Frontend with Streamlit**: A user-friendly frontend built with **Streamlit** for seamless interaction.

## How It Works
1. **Data Collection**:
   - IRCC webpages were scraped for work-permit-related content after obtaining permissions.
   - Extracted data was processed and converted into embeddings.

2. **Vector Search**:
   - Data embeddings were stored in **AstraDB** for fast and scalable retrieval.
   - User queries trigger a search for the top 5 most relevant documents based on their embeddings.

3. **Answer Generation**:
   - Retrieved documents are fed into SambaNova's LLM.
   - The LLM generates precise and well-structured answers based on the provided context.

4. **Frontend**:
   - Users interact with the chatbot through a **Streamlit-based UI**.
   - Queries are processed, and responses are displayed in real-time.

## Technologies Used
- **Web Scraping**: Extracting IRCC webpage data.
- **DataStax AstraDB**: Storing and retrieving embeddings.
- **SambaNova LLM**: Generating high-quality responses.
- **llama-index**: Building the RAG pipeline.
- **Streamlit**: Developing the interactive user interface.

## [Try it yourself](https://huggingface.co/spaces/gruhit-patel/ircc-work-permit-chat-bot)

## Demo
[ircc_work_permit_chatbot.webm](https://github.com/user-attachments/assets/d8f2b944-31bd-494f-a811-fec4cc8ca316)

## Future Work
- Make the response generation faster
- Increase the model accuracy.

## Disclaimer
⚠️ **Disclaimer**:
The chatbot's responses are generated based on scraped IRCC webpage data and may not always be accurate or up-to-date. For the most reliable information, please consult the official IRCC website at [IRCC Website]([https://www.canada.ca/immigration](https://www.canada.ca/en/immigration-refugees-citizenship/services/work-canada/permit.html)).

## Contact
For any questions or issues, feel free to reach out:
- **Email**: [gruhitspatel15@gmail.com]
- **GitHub**: [https://github.com/Gruhit13]

---

Enjoy using the IRCC Work-Permit Chatbot!
