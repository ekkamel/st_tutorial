# https://www.youtube.com/watch?v=VqgUkExPvLY&list=PLa182d3BzpdIyCqFILln9CLE5Y7CNmSqk&index=122&t=463s

import streamlit as st

# Find more emoji here:  https://webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- HEADER SECTION ----
with st.container(): 
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst from Germany")
    st.write("I am passionate about finding ways to Python and VBA to be more efficient")
    st.write("[Learn More >](https://pythonandvba.com)")

    # ---- WHAT I DO ----
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column: 
            st.header("What I do")
            st.write("##")
            st.write(
                """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."
            
            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
                """
            )