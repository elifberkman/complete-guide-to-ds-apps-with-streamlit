### DO NOT USE!!! Try st.session_state instead.
### https://docs.streamlit.io/library/api-reference/session-state

import streamlit as st
from streamlit_embedcode import github_gist
import SessionState
from decouple import config

PASSWORD = config("PASSWORD")
session_state = SessionState.get(password="")


def use_component():
    gist_link = st.text_input("https://gist.github.com/elifberkman/f94649370c54ee5686a11cb931ad01f0")
    github_gist(gist_link, width=730)


if (session_state.password == PASSWORD):
    use_component()
elif (session_state.password != PASSWORD):
    password_placeholder = st.empty()
    password = password_placeholder.text_input("Enter Password", type="password")
    session_state.password = password
    if (password and session_state.password == PASSWORD):
        password_placeholder.empty()
        st.success("Logged in Successfully")
        use_component()
    elif (password and session_state.password != PASSWORD):
        st.error("Wrong Password")