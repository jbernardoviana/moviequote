import streamlit as st
from moviequote.lib import get_quote

quote = get_quote()

st.write("# Welcome to my movie quotes App! 🚀")
st.write("### Refresh the page to get a new quote! ")
st.write(f"{quote}")

st.write("Made with ❤️ in Lisbon")
