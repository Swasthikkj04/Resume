import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Swasthik's Resume", layout="wide")

# Custom CSS for Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        color: #333;
    }

    .title {
        font-size: 40px;
        font-weight: 700;
        color: #4B8BBE;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        font-weight: 600;
        color: #306998;
        text-align: center;
    }
    .section-title {
        font-size: 26px;
        font-weight: 600;
        color: #1F4E79;
        margin-top: 30px;
        padding-bottom: 10px;
        border-bottom: 2px solid #1F4E79;
    }
    .section-content {
        font-size: 18px;
        color: #555;
        margin-top: 15px;
        line-height: 1.5;
    }
    .small-text {
        font-size: 16px;
        color: #555;
    }
    .link {
        color: #306998;
        text-decoration: none;
        font-weight: 600;
    }
    .link:hover {
        text-decoration: underline;
    }
    .icon {
        font-size: 18px;
        margin-right: 8px;
    }

    /* Button Styles */
    .stDownloadButton {
        background-color: #4B8BBE;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        text-align: center;
        font-weight: 600;
        cursor: pointer;
    }

    .stDownloadButton:hover {
        background-color: #306998;
    }

    /* Hover effect for Projects */
    .project-item:hover {
        color: #306998;
        cursor: pointer;
    }

    </style>
""", unsafe_allow_html=True)

# ---- HEADER ----
col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.png", width=150)  # Add your photo as "profile.jpg"
with col2:
    st.markdown('<div class="title">Swasthik K J</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">AI & ML Enthusiast | Python Freak | Full Stack Developer</div>', unsafe_allow_html=True)
    st.write("📍 Shivamogga, Karnataka, India")
    st.write("📧 swasthikkjgowda2004@gmail.com | 🌐 [GitHub](https://github.com/Swasthikkj04) | 🔗 [LinkedIn](https://www.linkedin.com/in/swasthik-k-j-9234242a6/)")

# ---- ABOUT ----
st.markdown('<div class="section-title">🧠 About Me</div>', unsafe_allow_html=True)
st.markdown("""
I am an enthusiastic and driven student of **Artificial Intelligence and Machine Learning**, with a strong passion for creating intelligent systems that solve real-world problems. My journey involves working on various **AI-driven applications** such as language processing, data analysis, and developing **smart solutions** that integrate into people's daily lives.
""", unsafe_allow_html=True)

# ---- SKILLS ----
st.markdown('<div class="section-title">🛠️ Skills</div>', unsafe_allow_html=True)
cols = st.columns(3)
cols[0].markdown("- Python, C, Java (basic)")
cols[0].markdown("- Data Structures, Algorithms")
cols[1].markdown("- Machine Learning")
cols[2].markdown("- Streamlit, Flutter, Flask, Firebase")

# ---- PROJECTS ----
st.markdown('<div class="section-title">📂 Projects</div>', unsafe_allow_html=True)

project_list = [
    ("📚 **Japanese Handwritten Digit Recognition**", "Trained on Kuzushiji-MNIST with Keras for digit classification."),
    ("🛒 **RFID Smart Cart**", "Automatic item tracking using UHF RFID and mobile app integration."),
    ("🧑‍🏫 **AI Language Tutor**", "Grammar and vocabulary suggestions using NLP and discourse analysis."),
    ("💬 **LangChain Offline Chatbot**", "A chatbot powered by LangChain to answer specific queries without API calls.")
]

for title, desc in project_list:
    st.markdown(f'<div class="project-item"><strong>{title}</strong> — {desc}</div>', unsafe_allow_html=True)

# ---- EDUCATION ----
st.markdown('<div class="section-title">🎓 Education</div>', unsafe_allow_html=True)
st.markdown("""
**B.E in Artificial Intelligence & Machine Learning**  
PESITM, VTU – 2022–2026
""")

# ---- CERTIFICATIONS ----
st.markdown('<div class="section-title">🎓 Certifications</div>', unsafe_allow_html=True)
st.markdown("""
- **Basics of Python Programming** – Great Learning
- **Machine Learning with Python** – Great Learning
- **Deep Learning with PyTorch** – IBM
- **Fundamentals of MongoDB** – MongoDB University
""")

# ---- DOWNLOAD RESUME BUTTON ----
st.markdown('<div class="section-title">📄 Download Resume</div>', unsafe_allow_html=True)
with open("Swasthik_Resume.pdf", "rb") as file:
    st.download_button(label="Download PDF", data=file, file_name="Swasthik_Resume.pdf", mime="application/pdf", use_container_width=True)

# ---- CONTACT INFO ----
st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)
st.markdown("""
Feel free to reach out to me via email or connect on LinkedIn for collaborations or job opportunities!
""", unsafe_allow_html=True)
