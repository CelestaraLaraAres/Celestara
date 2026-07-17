import streamlit as st

st.set_page_config(page_title="Celestara", page_icon="✨")
st.markdown("<h1 style='text-align: center;'>Celestara</h1>", unsafe_allow_html=True)

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
        st.markdown(f"*{karakter} şu an dinleniyor. Yarın kota yenilendiğinde aktif olacak.*")
