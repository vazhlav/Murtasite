import streamlit as st  #st es el short para streamline ( as permite crear un alias)
# correr streamlit en browser >streamlit run archivo.py
import google.generativeai as genai
import os
#hide apikey fo security
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Vazhlav Lastra")

with col2:
    st.image("images/PSX_20221013_021420.jpg")

st.title(" ")   #blank space vertical
#secret sauce of logic
persona = """Escultor Mexicano
Hola, mi nombre es Vazhlav Lastra Flores soy artista plástico, escultor y creativo multidisciplinario.
Artes plásticas, diseño industrial, upcycling, interiores, hasta medios digitales por mencionar algunos, 
tengo particular gusto por la tecnología, ciencias y otras.
Realizo mis trabajos e investigaciones personalmente."""

st.title("Vazh AI Bot")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400): #use_container_width=100 ajusta el largo del boton
    prompt = persona + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

#secret sauce

st.title(" ")   #blank space vertical

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Art Channel")
    st.write("- 20 years of knowledge")
    st.write("- Hitchhikers guide to Art Galaxy")
    st.write("- Language: Spanish (Mexico)")

with col2:
    st.video("https://youtu.be/mz-WyolC-YQ")

st.title(" ")
st.title("My Setup")
st.image("images/PSX_20221013_021420.jpg")

st.title(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 50)
st.slider("Is", 0, 100, 100)
st.slider("Fun", 0, 100, 10)

st.title(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")

with col1:
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")

with col1:
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")

st.title(" ")
st.title("CONTACT")

# Supported languages
languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
}

def set_language(language):
    if language == 'en':
        st.session_state.language = 'en'
    elif language == 'es':
        st.session_state.language = 'es'
    elif language == 'fr':
        st.session_state.language = 'fr'
    elif language == 'de':
        st.session_state.language = 'de'

# Set language based on user selection or default to English
if 'language' not in st.session_state:
    st.session_state.language = 'en'

# Language selection dropdown
selected_language = st.sidebar.selectbox(
    "Select language:",
    list(languages.keys()),
    index=list(languages.values()).index(st.session_state.language)
)

set_language(languages[selected_language])

# Conditional content based on selected language
if st.session_state.language == 'en':
    st.title("English Website")
    st.write("This is the content in English.")

elif st.session_state.language == 'es':
    st.title("Sitio web en español")
    st.write("Este es el contenido en español.")

elif st.session_state.language == 'fr':
    st.title("Site Web en français")
    st.write("Voici le contenu en français.")

elif st.session_state.language == 'de':
    st.title("Website auf Deutsch")
    st.write("Dies ist der Inhalt auf Deutsch.")
st.title("For any inquiries, please contact me")
st.subheader("Visit: vazhlav.com")



