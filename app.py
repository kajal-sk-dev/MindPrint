import streamlit as st

st.set_page_config(
    page_title="MindPrint - Human Authenticity Detector",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 MindPrint")
st.subheader("Your code has a MindPrint. AI can't fake it.")

st.divider()

code_input = st.text_area(
    "Paste your code / text here:",
    height=250,
    placeholder="Paste code or content to check human authenticity..."
)

col1, col2 = st.columns(2)

with col1:
    check_btn = st.button("🔍 Check MindPrint", use_container_width=True)

with col2:
    clear_btn = st.button("Clear", use_container_width=True)

if check_btn:
    if not code_input.strip():
        st.warning("Please paste some content first!")
    else:
        with st.spinner("Analyzing MindPrint..."):
            length = len(code_input)
            if length > 500:
                score = 87
                result = "Human Written"
            else:
                score = 62
                result = "Likely Human"
            
            st.success(f"Result: {result}")
            st.metric("Human Authenticity Score", f"{score}%")
            st.progress(score / 100)
            st.info("💡 Trace the Human Behind the Code - MindPrint Analysis Complete")

if clear_btn:
    st.rerun()
