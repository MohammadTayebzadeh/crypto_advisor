import google.generativeai as genai
import streamlit as st
import re 


def gemini(prompt):
    genai.configure(api_key = st.secrets["general"]["GOOGLE_API_KEY"])
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return (response.text)


def ai(prompt):
    response_text = gemini(prompt)

    # استفاده از re برای تبدیل تیترهای ## به HTML <h2>
    response_text = re.sub(r"##\s*(.*)", r"<h2 style='text-align: right; direction: rtl; font-family: \"IRANSans\", sans-serif;'>\1</h2>", response_text)

    # تغییرات نهایی در متغیر
    styled_text = f"""
    <div style='text-align: right; direction: rtl; font-family: "IRANSans", sans-serif;'>
        {response_text}
    </div>
    """

    # نمایش متن در Streamlit
    st.markdown(styled_text, unsafe_allow_html=True)
