CodeAlpha FAQ Chatbot



Project Overview



This project is an FAQ chatbot developed using Python. It helps users get answers to frequently asked questions through a simple interactive web interface.



Features



\- Interactive chatbot interface using Streamlit.

\- Predefined frequently asked questions and answers.

\- Text processing using TF-IDF vectorization.

\- Cosine similarity to identify the closest matching question.

\- Fallback response when a suitable answer is not found.

\- Chat history displayed during the session.



Technologies Used



\- Python

\- Streamlit

\- Scikit-learn

\- TF-IDF Vectorization

\- Cosine Similarity



How It Works



1\. The user enters a question in the chatbot.

2\. The chatbot converts the question into a numerical representation using TF-IDF.

3\. Cosine similarity compares it with the stored FAQ questions.

4\. The chatbot displays the answer corresponding to the closest match.

5\. If the similarity score is too low, it asks the user to try another question.



How to Run



1\. Install Python 3.11 or a compatible version.



2\. Install the required libraries:

&#x20;  

&#x20;  "pip install streamlit scikit-learn"



3\. Run the application:

&#x20;  

&#x20;  "streamlit run app.py"



4\. Open the local URL displayed in the terminal.



Project Purpose



Created as part of the CodeAlpha Artificial Intelligence Internship to demonstrate a basic FAQ chatbot using natural language processing techniques.

