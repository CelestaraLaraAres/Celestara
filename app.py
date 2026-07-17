
import streamlit as st
import google.generativeai as genai
import os

# API anahtarını güvenli bir şekilde al
api_key = st.secrets.get("GOOGLE_API_KEY")

if not api_key:
    st.error("Hata: GOOGLE_API_KEY bulunamadı! Lütfen Streamlit Secrets ayarlarını kontrol et.")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')

# ... kodunun geri kalanı aynı şekilde devam etsin ...
st.set_page_config(page_title="Celestara", page_icon="✨")
st.markdown("<h1 style='text-align: center;'>Celestara</h1>", unsafe_allow_html=True)

# API anahtarını tanımla
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
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
        # Yapay zekaya karakteri tanımlayarak mesajı gönderiyoruz
        response = model.generate_content(f"Sen {karakter} isimli bir asistansın. Kullanıcıya bu karakterin kişiliğiyle cevap ver: {prompt}")
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
