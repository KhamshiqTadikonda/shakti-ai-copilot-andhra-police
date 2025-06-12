import streamlit as st
import openai

st.set_page_config(page_title="SHAKTI - FIR Summarizer", layout="centered")

st.title("📄 SHAKTI - FIR Summarizer for Andhra Police")

openai.api_key = st.secrets["OPENAI_API_KEY"]

fir = st.text_area("Paste FIR content here:")

if st.button("Summarize FIR"):
    with st.spinner("Analyzing FIR..."):
        prompt = f"Summarize this FIR into 3 bullet points with focus on who, what, and where: {fir}"
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        summary = response['choices'][0]['message']['content']
        st.success("AI-Generated Summary:")
        st.write(summary)
