# Gemini-Quizify Missions

This project consists of a series of tasks designed to create an interactive quiz builder application using Streamlit, LangChain, and Google Cloud Vertex AI. The application allows users to upload documents, generate embeddings, create a vector store (Chroma collection), and generate quiz questions based on the uploaded documents.

## Tasks Overview

### Task 3: Document Processor
**Objective:** Develop a class to process uploaded PDF documents using Streamlit and LangChain's PyPDFLoader.

**Details:**
- Users can upload multiple PDF files.
- Each uploaded PDF file is processed to extract its pages.
- Extracted pages are stored in a list.
- The total number of pages processed is displayed.

### Task 4: Embedding Client
**Objective:** Create a class to initialize and interact with Google Cloud's Vertex AI for generating text embeddings.

**Details:**
- Initialize the embedding client with model name, project ID, and location.
- Provide methods to embed single text queries and multiple documents.
- Display the embeddings using Streamlit.

### Task 5: Chroma Collection Creator
**Objective:** Create a class to generate a Chroma collection from processed documents using LangChain's CharacterTextSplitter and Vertex AI embeddings.

**Details:**
- Check if any documents have been processed.
- Split the processed documents into smaller text chunks.
- Create a Chroma collection from the text chunks and embeddings.
- Display success or error messages based on the collection creation process.

### Task 6: Quiz Builder Integration
**Objective:** Integrate components from previous tasks to create a "Quiz Builder" application in Streamlit.

**Details:**
- Initialize `DocumentProcessor` and process uploaded documents.
- Configure and initialize `EmbeddingClient`.
- Instantiate `ChromaCollectionCreator`.
- Create a form to input the quiz topic and number of questions.
- Generate a Chroma collection and retrieve relevant information for quiz generation.

### Task 7: Quiz Generator Initialization
**Objective:** Initialize a class to generate quiz questions using the topic provided and context from the Chroma collection.

**Details:**
- Set up and configure the Large Language Model (LLM) with model name, temperature, and max output tokens.
- Ensure the vector store is initialized and retrieve relevant documents.
- Format the context and topic into a structured prompt.
- Use the LLM to generate quiz questions.

### Task 8: Quiz Generation
**Objective:** Develop a method to generate a list of unique quiz questions based on the specified topic and number of questions.

**Details:**
- Generate quiz questions using the LLM and vector store.
- Validate the uniqueness of each question.
- Store valid and unique questions in a question bank.

### Task 9: Quiz Manager
**Objective:** Create a class to manage the generated quiz questions and facilitate navigation through the quiz.

**Details:**
- Initialize the `QuizManager` class with a list of quiz questions.
- Provide methods to retrieve questions by index and navigate through the quiz.
- Display generated quiz questions in Streamlit with multiple-choice options.

### Task 10: Complete Quiz Application
**Objective:** Integrate all components to build a fully functional quiz application.

**Details:**
- Combine `DocumentProcessor`, `EmbeddingClient`, `ChromaCollectionCreator`, and `QuizGenerator`.
- Use `QuizManager` to manage and display quiz questions.
- Implement a user interface in Streamlit for uploading documents, generating quizzes, and navigating through questions.

## How to Use
1. **Document Upload and Processing:**
   - Upload PDF documents.
   - The documents will be processed to extract pages.

2. **Embedding and Chroma Collection Creation:**
   - Configure the embedding client with model name, project ID, and location.
   - Create a Chroma collection from the processed documents.

3. **Quiz Generation:**
   - Input the quiz topic and the number of questions.
   - Generate quiz questions based on the topic and document context.

4. **Quiz Management:**
   - Display generated quiz questions.
   - Navigate through questions and provide answers.

## Installation
To run this project locally, follow these steps:

1. Clone the repository.
   ```sh
   git clone <repository_url>
   cd gemini-quizify


#Installing Dependencies
To install dependencies run:
```python
pip install -r requirements.txt
```

To run the streamlit application:
```python
streamlit run <task_name>.py
```
