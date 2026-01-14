# RUN COMMAND : streamlit run app.py
# RUN COMMAND : streamlit run app.py
# RUN COMMAND : streamlit run app.py
import streamlit as st
from pypdf import PdfReader
import re
import time

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="PDF Clean Text Pro",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #ffffff;
}

.main-title {
    font-size: 3rem;
    font-weight: 800;
    text-align: center;
    margin-bottom: 0.2em;
}

.subtitle {
    text-align: center;
    font-size: 1.2rem;
    opacity: 0.8;
    margin-bottom: 2em;
}

.card {
    background: rgba(255,255,255,0.05);
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}

.card:hover {
    transform: scale(1.02);
}

.metric {
    font-size: 1.6rem;
    font-weight: bold;
}

.footer {
    text-align: center;
    opacity: 0.6;
    margin-top: 3em;
}
</style>
""", unsafe_allow_html=True)

# ------------------ FUNCTIONS ------------------
def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r' \n', '\n', text)
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)

def show_loader():
    with st.spinner("Processing PDF..."):
        time.sleep(1.2)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">📄 PDF Clean Text Pro</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Extract • Clean • Analyze PDF text like a pro</div>', unsafe_allow_html=True)

# ------------------ UPLOAD ------------------
uploaded_file = st.file_uploader("Upload your PDF file", type=["pdf"])

if uploaded_file:
    show_loader()

    reader = PdfReader(uploaded_file)
    raw_text = ""

    for page in reader.pages:
        raw_text += page.extract_text() + "\n"

    cleaned_text = clean_text(raw_text)

    # ------------------ STATS ------------------
    word_count = len(cleaned_text.split())
    char_count = len(cleaned_text)
    line_count = len(cleaned_text.split('\n'))
    page_count = len(reader.pages)

    st.markdown("## 📊 Document Statistics")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown(f"<div class='card'><div class='metric'>{page_count}</div>Pages</div>", unsafe_allow_html=True)
    col2.markdown(f"<div class='card'><div class='metric'>{word_count}</div>Words</div>", unsafe_allow_html=True)
    col3.markdown(f"<div class='card'><div class='metric'>{char_count}</div>Characters</div>", unsafe_allow_html=True)
    col4.markdown(f"<div class='card'><div class='metric'>{line_count}</div>Lines</div>", unsafe_allow_html=True)

    # ------------------ OUTPUT ------------------
    st.markdown("## 🧹 Cleaned Text Output")
    st.text_area("Result", cleaned_text, height=350)

    st.download_button(
        label="⬇️ Download Cleaned Text",
        data=cleaned_text,
        file_name="cleaned_text.txt",
        mime="text/plain"
    )

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">Built with Python • Streamlit • PDF Intelligence</div>', unsafe_allow_html=True)
