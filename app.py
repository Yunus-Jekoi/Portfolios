import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Yunus's Portfolio", page_icon=":computer:", layout="centered")

# Custom HTML for the box around the content
st.markdown(
    """
    <div style="max-width: 800px; margin: 0 auto; padding: 20px; border: 1px solid black; border-radius: 10px; text-align: center; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h1 style="color: black; font-weight: bold;">Hi, I am Yunus 👋</h1>
        <h2 style="color: black; font-weight: bold;">A software engineer in the U.S.</h2>
        <p style="color: black; font-weight: bold;">I am passionate about finding ways to use Python in a way to automate and help others ❤️</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---- ABOUT ME SECTION ----
st.markdown(
    """
    <div style="max-width: 800px; margin: 20px auto; padding: 20px; border: 1px solid black; border-radius: 10px; text-align: center; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <h2 style="color: black; font-weight: bold;">About Me 🧑‍💻</h2>
        <p style="color: black; font-weight: bold;">I have a passion for technology and a strong background in coding.</p>
        <p style="color: black; font-weight: bold;">I love using Python to create automated solutions and help others improve their workflows.</p>
        <p style="color: black; font-weight: bold;">When I'm not coding, I enjoy travelling, cars, and exploring new technologies.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
