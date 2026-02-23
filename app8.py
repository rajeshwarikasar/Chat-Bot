import streamlit as st
import google.generativeai as genai
import time

# Page configuration
st.set_page_config(page_title="GenAI Chatbot", page_icon="🤖", layout="wide")

# Custom CSS for background and chat styling
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
        font-family: 'Trebuchet MS', sans-serif;
    }
    .main-title {
        text-align: center;
        color: white;
        font-size: 50px;
        font-weight: bold;
        text-shadow: 2px 2px 5px #000000;
        margin-bottom: 20px;
    }
    .chat-bubble-user {
        background-color: #4CAF50;
        color: white;
        padding: 12px;
        border-radius: 15px;
        margin: 8px;
        max-width: 70%;
        float: right;
        clear: both;
    }
    .chat-bubble-bot {
        background-color: #ffffff;
        color: #333333;
        padding: 12px;
        border-radius: 15px;
        margin: 8px;
        max-width: 70%;
        float: left;
        clear: both;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<div class='main-title'>✨ Welcome to my GenAI Application ✨</div>", unsafe_allow_html=True)

# Sidebar decoration
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=150)
st.sidebar.markdown("### 🌈 Features")
st.sidebar.write("- AI-powered responses")
st.sidebar.write("- Sleek design with gradient background")
st.sidebar.write("- Animated typing effect")
st.sidebar.write("- Stylish chat bubbles")

# Configure GenAI
genai.configure(api_key="AIzaSyBakkH-fZNJp5SSGfzbOI7FNzg7sByQOYM")
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input
user = st.chat_input("💬 Ask me anything:")

if user:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user})

    # Generate response
    response = model.generate_content(user)
    bot_reply = response.text

    # Add bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

# Display chat history with styled bubbles
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        # Animated typing effect
        placeholder = st.empty()
        animated_text = ""
        for char in msg["content"]:
            animated_text += char
            time.sleep(0.01)  # typing speed
            placeholder.markdown(f"<div class='chat-bubble-bot'>{animated_text}</div>", unsafe_allow_html=True)

# Extra decoration: tabs as slides
tab1, tab2, tab3 = st.tabs(["🌟 About", "📸 Gallery", "🎨 Style"])

with tab1:
    st.write("This chatbot is powered by Google's Gemini model and Streamlit UI.")
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", caption="Your AI Companion")

with tab2:
    st.image("https://picsum.photos/600/300", caption="Random Inspiration")
    st.image("https://picsum.photos/600/301", caption="Creative Energy")

with tab3:
    st.markdown(
        "<div style='background-color:#ffe4e1; padding:20px; border-radius:10px;'>"
        "<h3 style='color:#ff1493;'>Custom Styling</h3>"
        "<p>Decorate your chatbot with vibrant colors, fonts, and layouts to make it more engaging.</p>"
        "</div>",
        unsafe_allow_html=True
    )