import streamlit as st
from checker import check_updates
from mailer import send_email

st.set_page_config(page_title="Dependency Update Notifier", layout="wide")
st.title("📦 Python Dependency Update Checker")

if st.button("🔍 Check Now"):
    report = check_updates()
    if not report:
        st.success("✅ All dependencies are up to date!")
    else:
        st.warning(f"⚠️ {len(report)} outdated dependencies found.")
        st.table(report)

        if st.button("📬 Send Email Notification"):
            send_email(report, to_email="recipient@example.com")
            st.info("✅ Email sent successfully.")
