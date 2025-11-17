import streamlit as st

st.title("テスト")
st.write("Hello World!")

name = st.text_input("名前を入力")
if st.button("挨拶"):
    st.success(f"こんにちは、{name}さん！")
