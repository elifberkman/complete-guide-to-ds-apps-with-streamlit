import streamlit as st
from streamlit_embedcode import github_gist

gist_link = st.text_input("Enter link")
# Example link: "https://gist.github.com/elifberkman/f94649370c54ee5686a11cb931ad01f0"
if gist_link != "":
    github_gist(gist_link, width=730)