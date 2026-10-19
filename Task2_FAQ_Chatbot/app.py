import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="FAQ Chatbot",
    page_icon="🤖"
)

st.title("🤖 FAQ Chatbot")
st.write("Ask me anything about our services!")

faqs = {
    "What is your name?": "I am an FAQ Chatbot, here to help you.",
    "What are your working hours?": "Our working hours are 9 AM to 5 PM, Monday to Friday.",
    "How can I contact support?": "You can contact our support team through email.",
    "How can I reset my password?": "Click on Forgot Password on the login page and follow the instructions.",
    "What services do you provide?": "We provide information and assistance to help users with their queries.",
    "How can I register?": "Click the Sign Up button and fill in the required details.",
    "Is your service free?": "Yes, this demo chatbot is free to use.",
    "How can I give feedback?": "You can share your feedback through our feedback section."
}

questions = list(faqs.keys())
answers = list(faqs.values())

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Type your question here...")

if user_question:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    user_vector = vectorizer.transform([user_question])
    similarities = cosine_similarity(
        user_vector, question_vectors
    )[0]

    best_match = similarities.argmax()

    if similarities[best_match] >= 0.25:
        response = answers[best_match]
    else:
        response = (
            "Sorry, I couldn't find a suitable answer. "
            "Please try asking another question."
        )

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.write(response)