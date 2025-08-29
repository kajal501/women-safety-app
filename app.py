import streamlit as st

# Title
st.set_page_config(page_title="Women Safety App", page_icon="🚨", layout="centered")
st.markdown("<h1 style='text-align: center; color: #E75480;'>🚨 Women Safety App 🚨</h1>", unsafe_allow_html=True)

st.write("Your safety is our priority. Please enter your details below:")

# Input fields
location = st.text_input("📍 Enter Your Current Location")
contact = st.text_input("📞 Enter Emergency Contact Name/Number")

# Alert Button
if st.button("Send Alert 🚨"):
    if location and contact:
        st.success(f"🚨 Emergency Alert Sent!\n\n📍 Location: {location}\n📞 Contact: {contact}")
    else:
        st.warning("⚠️ Please enter both location and contact details before sending an alert.")

# Footer
st.markdown("<br><hr><center>Prototype for Hackathon - Women Safety</center>", unsafe_allow_html=True)


