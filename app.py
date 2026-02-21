import streamlit as st

st.markdown(
    """
    <style>
    /* ------------------------------
       Animated Pink Gradient Background
    ------------------------------ */
    .stApp {
        background: linear-gradient(
            -45deg,
            #fff0f6,
            #ffd6e7,
            #ffe3ec,
            #fcc2d7
        );
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* ------------------------------
       Title
    ------------------------------ */
    h1 {
        color: #880e4f !important;
        text-align: center;
        font-weight: 800;
    }

    /* ------------------------------
       ALL LABEL TEXT (FIX)
    ------------------------------ */
    label, 
    .stSelectbox label, 
    .stTextArea label,
    .stMarkdown,
    .stCaption {
        color: #5a0036 !important;
        font-weight: 600;
    }

    /* ------------------------------
       Selectbox / Input Text
    ------------------------------ */
    select, textarea, input {
        color: #4a004e !important;
        background-color: #fff5f8 !important;
        border-radius: 12px !important;
        border: 2px solid #f783ac !important;
    }

    /* Placeholder text */
    textarea::placeholder, input::placeholder {
        color: #a61e4d !important;
    }

    /* ------------------------------
       Buttons
    ------------------------------ */
    div.stButton > button {
        background: linear-gradient(135deg, #ff69b4, #e64980);
        color: white;
        border-radius: 12px;
        border: none;
        padding: 0.6em 1.4em;
        font-weight: bold;
        transition: all 0.3s ease-in-out;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #e64980, #c2255c);
    }

    /* ------------------------------
       Code Blocks
    ------------------------------ */
    pre {
        background-color: #fff0f6 !important;
        color: #4a004e !important;
        border-radius: 12px;
        border: 2px solid #faa2c1;
    }

    /* ------------------------------
       Expanders (History)
    ------------------------------ */
    details {
        background-color: #ffe3ec;
        border-radius: 14px;
        padding: 12px;
        border: 2px solid #faa2c1;
    }

    details summary {
        color: #880e4f;
        font-weight: bold;
    }

    /* ------------------------------
   Cursor (Caret) Visibility FIX
    ------------------------------ */
    textarea, input {
    caret-color: #880e4f !important;  /* dark pink cursor */
    }
    /* ------------------------------
   Animated Focus Border & Soft Glow
    ------------------------------ */

    /* Default input transition */
    textarea, input, select {
        transition: 
            border-color 0.3s ease,
            box-shadow 0.3s ease,
            transform 0.15s ease;
    }

    /* Focus effect */
    textarea:focus, 
    input:focus, 
    select:focus {
        outline: none !important;
        border-color: #e64980 !important;
        box-shadow: 
            0 0 0 2px rgba(230, 73, 128, 0.25),
            0 0 12px rgba(230, 73, 128, 0.45);
        transform: scale(1.01);
    }

    /* Extra smooth glow pulse (subtle) */
    @keyframes softGlow {
        0% {
            box-shadow: 0 0 8px rgba(230, 73, 128, 0.35);
        }
        50% {
            box-shadow: 0 0 14px rgba(230, 73, 128, 0.6);
        }
        100% {
            box-shadow: 0 0 8px rgba(230, 73, 128, 0.35);
        }
    }

    /* Apply animation only while focused */
    textarea:focus,
    input:focus {
        animation: softGlow 1.8s ease-in-out infinite;
    }
        </style>
    """,
    unsafe_allow_html=True
)
from prompts import (
    generate_code,
    explain_code,
    explain_code_simple,
    debug_code,
    explain_concept
)
from llm import ask_llm

st.set_page_config(page_title="AI Coding Bot", layout="centered")
st.title("🤖 AI Coding Bot")

# -------------------------------
# Session State
# -------------------------------
if "last_prompt" not in st.session_state:
    st.session_state.last_prompt = None
if "last_reply" not in st.session_state:
    st.session_state.last_reply = None

# -------------------------------
# Mode Selection
# -------------------------------
option = st.selectbox(
    "Choose a function",
    [
        "Generate Code",
        "Explain Code",
        "Explain Simply",
        "Debug Code",
        "Explain Concept"
    ]
)

prompt = None

# -------------------------------
# Generate Code
# -------------------------------
if option == "Generate Code":
    language = st.selectbox(
        "Select Programming Language",
        ["Python", "Java", "C", "C++", "JavaScript"]
    )

    level = st.selectbox(
        "Select Difficulty Level",
        ["Beginner", "Intermediate", "Advanced"]
    )

    user_input = st.text_area("Enter the problem statement")

    if user_input:
        prompt = generate_code(language, user_input, level)

# -------------------------------
# Explain Code
# -------------------------------
elif option == "Explain Code":
    user_input = st.text_area("Paste the code")
    if user_input:
        prompt = explain_code(user_input)

# -------------------------------
# Explain Simply
# -------------------------------
elif option == "Explain Simply":
    user_input = st.text_area("Paste the code")
    if user_input:
        prompt = explain_code_simple(user_input)

# -------------------------------
# Debug Code
# -------------------------------
elif option == "Debug Code":
    code = st.text_area("Paste the code")
    error = st.text_area("Paste the error message")

    if code and error:
        prompt = debug_code(code, error)

# -------------------------------
# Explain Concept
# -------------------------------
elif option == "Explain Concept":
    concept = st.text_area("Enter the concept (e.g., recursion, OOP, stack)")
    if concept:
        prompt = explain_concept(concept)

# -------------------------------
# Buttons
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Ask Bot", key="ask_bot"):
        if prompt:
            st.session_state.last_prompt = prompt
            st.session_state.last_reply = ask_llm(prompt)
        else:
            st.warning("Please provide required input.")

with col2:
    if st.button("Regenerate", key="regen_bot"):
        if st.session_state.last_prompt:
            st.session_state.last_reply = ask_llm(st.session_state.last_prompt)

with col3:
    if st.button("Clear", key="clear_bot"):
        st.session_state.last_prompt = None
        st.session_state.last_reply = None
        st.rerun()

# -------------------------------
# Output
# -------------------------------
if st.session_state.last_reply:
    st.subheader("Bot Response")
    st.code(st.session_state.last_reply)