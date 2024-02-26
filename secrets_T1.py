import streamlit as st
# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB userid:", st.secrets["db_userid"])
st.write("DB password:", st.secrets["db_password"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
    os.environ["db_userid"] == st.secrets["db_userid"],
)
st.write( os.environ["db_username"] + "：" + os.environ["db_userid"] )
