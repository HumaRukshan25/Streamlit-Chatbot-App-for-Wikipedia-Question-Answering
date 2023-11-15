import streamlit as st
from wikipediaapi import Wikipedia
from transformers import pipeline

# Function to retrieve content from Wikipedia
def get_wikipedia_content(page_url):
    wiki_wiki = Wikipedia("en")
    page_py = wiki_wiki.page(page_url)
    return page_py.text

# Function to perform question-answering on Wikipedia content
def ask_question_wikipedia(content, question):
    qa_pipeline = pipeline("question-answering")
    result = qa_pipeline(question=question, context=content)
    return result['answer']

# Streamlit App
def main():
    st.title("Wikipedia Chatbot App")

    # Allow users to upload Wikipedia link
    page_url = st.text_input("Enter Wikipedia Page URL:")
    
    if page_url:
        # Retrieve and parse the content of the Wikipedia article
        content = get_wikipedia_content(page_url)

        # Display the content
        st.subheader("Wikipedia Article Content:")
        st.write(content)

        # Allow users to ask questions
        question = st.text_input("Ask a Question:")
        
        if question:
            # Perform question-answering
            answer = ask_question_wikipedia(content, question)

            # Display the answer
            st.subheader("Chatbot Answer:")
            st.write(answer)

# Run the app
if __name__ == "__main__":
    main()
