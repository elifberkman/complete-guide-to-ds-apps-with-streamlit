import pandas as pd
import streamlit as st
import altair as alt

df = pd.read_csv("../data/ted.csv")

# * beta_columns is now simply columns - https://huggingface.co/spaces/albertvillanova/datasets-tagging/commit/e25cf024512282dc1e6a2d78eb79197295e803cf
# left_column, right_column = st.beta_columns(2)
left_column, right_column = st.columns(2)

chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="published_year:O",
        y="sum(views)",
        color="published_day",
        tooltip="sum(views)"
    )
    .properties(width=500, height=500)
    .interactive()
)

with left_column:
    st.altair_chart(chart)

with right_column:
    st.altair_chart(chart)

with st.container():
    st.altair_chart(chart)

with st.expander("Some Explanation"):
    st.write("Some other explanation")