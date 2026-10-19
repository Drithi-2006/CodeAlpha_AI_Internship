import streamlit as st
from deep_translator import MyMemoryTranslator
from deep_translator.exceptions import TranslationNotFound

st.set_page_config(
    page_title="Language Translator",
    page_icon="🌍",
    layout="centered"
)

st.title("🌍 Language Translation Tool")
st.write("Translate text from one language to another!")

languages = {
    "English": "en-GB",
    "Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Malayalam": "ml-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "French": "fr-FR",
    "Spanish": "es-ES",
    "German": "de-DE",
    "Japanese": "ja-JP",
    "Arabic": "ar-SA"

}

col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Translate from",
        list(languages.keys()),
        index=0
    )

with col2:
    target_language = st.selectbox(
        "Translate to",
        list(languages.keys()),
        index=1
    )

text_input = st.text_area(
    "Enter your text",
    placeholder="Type something to translate...",
    height=150
)

if st.button("Translate", type="primary", use_container_width=True):
    if not text_input.strip():
        st.warning("Please enter some text to translate.")

    elif source_language == target_language:
        st.warning("Please select two different languages.")

    else:
        try:
            translator = MyMemoryTranslator(
                source=languages[source_language],
                target=languages[target_language]
            )

            translated_text = translator.translate(text_input)

            st.subheader("Translated Text")
            st.success(translated_text)

            st.caption(
                f"{source_language} → {target_language}"
            )

        except Exception as error:
          st.error(f"Translation failed: {error}")
            