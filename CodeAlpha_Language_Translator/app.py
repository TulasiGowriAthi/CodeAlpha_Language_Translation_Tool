import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import os

# 1. Page Configuration (Makes the web app look modern and clean)
st.set_page_config(page_title="AI Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 AI Language Translation Tool")
st.markdown("Enter your text, choose your target language, and let AI do the rest!")
st.write("---")

# 2. Supported Languages Dictionary
LANGUAGES = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Hindi': 'hi',
    'Mandarin (Chinese)': 'zh-CN',
    'Arabic': 'ar',
    'Japanese': 'ja',
    'Russian': 'ru',
    'Telugu': 'te'
}

# 3. User Interface Components
text_to_translate = st.text_area("Enter the text you want to translate:", placeholder="Type something here...", height=150)

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Source Language (Auto-Detect supported):", ["auto"] + list(LANGUAGES.keys()))
with col2:
    target_lang = st.selectbox("Target Language:", list(LANGUAGES.keys()))

target_code = LANGUAGES[target_lang]
source_code = "auto" if source_lang == "auto" else LANGUAGES[source_lang]

st.write("")

# 4. Core Translation Logic
if st.button("✨ Translate Text", use_container_width=True):
    if text_to_translate.strip() == "":
        st.warning("⚠️ Please enter some text to translate first!")
    else:
        with st.spinner("Translating... Please wait..."):
            try:
                # Initialize the translator backend
                translator = GoogleTranslator(source=source_code, target=target_code)
                
                # Perform the translation
                translated_text = translator.translate(text_to_translate)
                
                # Display the Result
                st.success("🎉 Translation Complete!")
                st.subheader("Translated Output:")
                st.info(translated_text)
                
                st.write("---")
                st.subheader("🔊 Audio Presentation (Bonus Feature)")
                
                # 5. Text-to-Speech Feature (The Top 3 Performer Edge)
                tts = gTTS(text=translated_text, lang=target_code, slow=False)
                audio_file = "translated_audio.mp3"
                tts.save(audio_file)
                
                # Play the audio inside the Streamlit app
                st.audio(audio_file, format="audio/mp3")
                
                # Clean up the audio file from your local storage safely
                os.remove(audio_file)
                
            except Exception as e:
                st.error(f"An error occurred during translation: {e}")

st.write("---")
st.caption("Developed for CodeAlpha AI Internship • Powered by Streamlit & Deep-Translator")