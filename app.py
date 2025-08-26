import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

out_parser = StrOutputParser()

st.title("💬 An AI Code Reviewer")


user_input = st.text_area("Enter your Python code here ...", height=200)

chat_template = ChatPromptTemplate.from_messages([
    ("system",
     "You are an AI Code Reviewer. "
     "Your job is to check Python code for errors and improvements. "
     "Always return in this format:\n\n"
     "### Bug Report\n"
     "List of issues in the code.\n\n"
     "### Fixed Code\n"
     "Provide the corrected code block."),
    ("human", "{code}")
])

chat_model = ChatGoogleGenerativeAI(
    api_key=Your_GOOGle_API_KEY,
    model="gemini-2.0-flash"
)

if st.button("Generate"):
    chain = chat_template | chat_model | out_parser
    review = chain.invoke(user_input)

    # Split into sections
    if "### Bug Report" in review and "### Fixed Code" in review:
        bug_report = review.split("### Fixed Code")[0].replace("### Bug Report", "").strip()
        fixed_code = review.split("### Fixed Code")[1].strip()

        st.header("Code Review")
        
        # Bug Report
        st.subheader("🐞 Bug Report")
        st.write(bug_report)

        # Fixed Code (show with syntax highlighting)
        st.subheader("✅ Fixed Code")
        st.code(fixed_code, language="python")
    else:
        st.markdown(review.replace("\n", "  \n"))




