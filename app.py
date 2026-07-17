import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Celestara", page_icon="✨")
st.markdown("<h1 style='text-align: center;'>Celestara</h1>", unsafe_allow_html=True)

# Doğrudan anahtarı buraya gömüyoruz (Test amaçlı)
genai.configure(api_key="AQ.Ab8RN6Ig9AJLpMn2_G9-eUwQl6Ife0e-DbvDW5r2RCXUN_onrw")
model = genai.GenerativeModel('gemini-pro')

karakter = st.radio("İletişim Kurulacak Birim:", ["Lara", "Ares"], horizontal=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input(f"{karakter} ile konuş..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(f"Sen {karakter} isimli bir asistansın. Kişiliğinle cevap ver: {prompt}")
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Bir hata oluştu: {e}")
