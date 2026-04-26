import streamlit as st

st.set_page_config(page_title="Ghulam AI Social", layout="centered")

# Nastaliq Rendering & UI
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu&display=swap');
    .stApp { background-color: #064e3b; color: white; }
    .urdu-font { font-family: 'Noto Nastaliq Urdu', serif; direction: rtl; text-align: right; line-height: 2.0; font-size: 20px; }
    .action-bar { display: flex; justify-content: space-around; background: #059669; padding: 10px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📱 Ghulam AI Social")

# Email-Only Login
email = st.text_input("Enter Email to Login", placeholder="example@email.com")

if email:
    st.sidebar.success(f"User: {email}")
    st.sidebar.markdown("### VIP Level: 50")
    
    # Chat Input
    user_msg = st.text_input("Type your message / سوال لکھیں")
    
    if user_msg:
        # Success Toast on Generation
        st.toast("AI is generating response...", icon="🚀")
        
        # Urdu Response Placeholder
        st.markdown('<div class="urdu-font">غلام حسین اے آئی آپ کے سوال کا جواب تیار کر رہا ہے۔ براہ کرم انتظار کریں۔</div>', unsafe_allow_html=True)
        
        # Content Action Bar
        st.markdown('<div class="action-bar">', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.button("📥 Download")
        with c2: st.button("📋 Copy")
        with c3: st.button("📤 Share")
        st.markdown('</div>', unsafe_allow_html=True)

    # Live Camera Interaction
    st.divider()
    st.camera_input("Vision Analysis / کیمرہ")

    # Upgrade UI
    with st.expander("💎 Upgrade to VIP"):
        st.write("Send payment to unlock premium features:")
        st.info("Easypaisa: 03461785207 (Ghulam Hussain)")
  
