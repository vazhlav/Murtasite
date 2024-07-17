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

with col2:
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")

with col3:
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")
    st.image("images/PSX_20221013_021420.jpg")

st.title(" ")
st.title("CONTACT")

st.title("For any inquiries, please contact me")
st.subheader("Visit: vazhlav.com")



