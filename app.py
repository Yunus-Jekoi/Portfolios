import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Yunus's Portfolio", page_icon="🇾🇭", layout="centered")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #000000; /* Set background color to black */
        color: #ffffff; /* Set text color to white */
        font-family: 'Arial', sans-serif;
    }
    .container {
        max-width: 800px; /* Adjusted max-width for centered content */
        margin: 0 auto;
        padding: 20px;
        text-align: center; /* Center the content */
    }
    h1, h2, h3 {
        color: #ffffff; /* Set headings color to white */
    }
    .subheader {
        color: #ffffff; /* Set subheader color to white */
    }
    .project-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: center; /* Center the projects */
        margin-top: 20px;
    }
    .project {
        margin: 10px;
        padding: 20px;
        border: 1px solid #ffffff;
        border-radius: 10px;
        text-align: center;
        transition: box-shadow 0.3s ease-in-out;
        background-color: #333333; /* Dark background for project cards */
    }
    .project:hover {
        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.2);
    }
    img {
        max-width: 100%;
        border-radius: 10px;
    }
    .logo {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the custom logo from the provided link
st.markdown(
    """
    <div class="logo">
        <img src="https://drive.google.com/uc?export=download&id=1paMb07BQiLL2hf7k98D07HMIjSGF0o7S" alt="Custom Logo" width="200">
    </div>
    """,
    unsafe_allow_html=True
)

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Yunus :wave:")
    st.title("A software engineer in the U.S.")
    st.write(
        "I am passionate about finding ways to use Python in a way to automate and help others :heart:"
    )

# ---- ABOUT ME SECTION ----
with st.container():
    st.header("About Me 🧑‍💻")
    st.write(
        """
        Hi, I'm Yunus. I have a passion for technology and a strong background in software engineering.
        I love using Python to create automated solutions and help others improve their workflows.
        When I'm not coding, I enjoy hiking, reading, and exploring new technologies.
        """
    )
