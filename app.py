import streamlit as st
from core.study_plan import generate_study_plan
from core.email_draft import generate_email_drafts
from core.syllabus import summarize_syllabus

st.title("AI Study Assistant")

st.header("📚 Notes → Weekly Study Plan")
notes_input = st.text_area("Paste your messy notes here:", height=200)

if st.button("Generate Study Plan"):
    if notes_input.strip() == "":
        st.warning("Please paste some notes first.")
    else:
        with st.spinner("Generating your study plan..."):
            plan = generate_study_plan(notes_input)
        st.markdown(plan)

st.header("✉️ Email Reply Drafts")
situation_input = st.text_area("Describe the situation or paste the message:", height=150, key="email_input")

if st.button("Generate Email Drafts"):
    if situation_input.strip() == "":
        st.warning("Please describe the situation first.")
    else:
        with st.spinner("Drafting replies..."):
            drafts = generate_email_drafts(situation_input)
        st.markdown(drafts)

st.header("📝 Syllabus Task Summarizer")
syllabus_input = st.text_area("Paste your syllabus or assignment list:", height=200, key="syllabus_input")

if st.button("Summarize Tasks"):
    if syllabus_input.strip() == "":
        st.warning("Please paste syllabus text first.")
    else:
        with st.spinner("Summarizing tasks..."):
            summary = summarize_syllabus(syllabus_input)
        st.markdown(summary)

