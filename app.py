# https://www.youtube.com/watch?v=VqgUkExPvLY&list=PLa182d3BzpdIyCqFILln9CLE5Y7CNmSqk&index=122&t=463s

from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

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

    img_contact_form = Image.open("yt_contact_form.png")
    img_lottie_animation = Image.open("yt_lottie_animation.png")

    #---- PROJECTS ----
    with st.container(): 
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            # insert image
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Integrate Lottie Anmations Inside your streamlit app")
            st.write(
                """
                Learn how to use Lottie files in streamlit!
                """
            )
        st.markdown("[Watch Videos...](https://youtube.be/TX50itGoINE)")


