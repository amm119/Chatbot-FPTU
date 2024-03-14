# !pip instal streamlit
# chạy = lệnh trong terminal : streamlit run [tên file]
import streamlit as st

st.title("💬 Chatbot")
st.caption("Chatbot for FPTU")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "TÔI LÀ ..."}
    ]  # nội dung chào mừng

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    # prompt người dùng = st.session_state.messages
    # msg này là output của chatbot
    msg = "test"
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
