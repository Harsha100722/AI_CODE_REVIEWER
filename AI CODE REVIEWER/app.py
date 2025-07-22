import streamlit as st
from analyzer import run_analysis
from utils import detect_language
import os

with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<div class="title-bar">AI CodeAudit</div>', unsafe_allow_html=True)

modules_dir = "modules"
module_files = sorted([f for f in os.listdir(modules_dir) if f.endswith(".py") and not f.startswith("__")])
pretty_names = [f.replace("_", " ").replace(".py", "").title() for f in module_files]
modules_map = dict(zip(pretty_names, [f[:-3] for f in module_files]))

st.markdown("#### Upload your code file or paste code below:")

uploaded_file = st.file_uploader(
    "Choose a code file",
    type=["py", "js", "java", "cpp", "c", "cs", "php", "txt", "html", "ts", "go", "rb", "rs"],
    key="code_uploader"
)
file_code = ""
filename = None
if uploaded_file is not None:
    filename = uploaded_file.name
    try:
        file_code = uploaded_file.read().decode("utf-8")
    except Exception:
        st.warning("File decoding failed. Please upload a valid UTF-8 text/code file.", icon="⚠️")
        file_code = ""

text_code = st.text_area("Or paste code here:", height=220)
code = file_code if file_code else text_code

detected_lang = detect_language(code, filename) if code.strip() else ""

if code.strip():
    st.markdown(f'<div class="lang-detect">Detected Language: <b>{detected_lang}</b></div>', unsafe_allow_html=True)

selected_pretty = st.selectbox("Select analysis tool:", pretty_names)
run = st.button("Analyze")

if run and code.strip():
    result = run_analysis(modules_map[selected_pretty], code)
    st.markdown(f"<div class='result-container'>{result}</div>", unsafe_allow_html=True)
elif run:
    st.warning("Upload or paste code for analysis.", icon="⚠️")
