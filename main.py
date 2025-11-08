# main.py

import streamlit as st
from handlers import generate_image, get_files
from PIL import Image

st.set_page_config(page_title="AI Image Gallery", layout="wide")
st.title("🖼️ AI-Powered Image Gallery ✨")
st.markdown("Generate images with Hugging Face's FLUX model and browse your saved gallery.")

# ✅ Persistent input using Session State
if "user_prompt" not in st.session_state:
    st.session_state["user_prompt"] = ""

with st.form("prompt_form"):
    user_input = st.text_input(
        "Describe your image prompt:",
        value=st.session_state["user_prompt"],
        key="prompt_input",
        placeholder="Type anything... e.g. 'a futuristic city skyline at sunset'",
    )
    submitted = st.form_submit_button("Generate")

if submitted:
    st.session_state["user_prompt"] = user_input  # Save last input
    with st.spinner("Generating your image... please wait ⌛"):
        try:
            image_path = generate_image(user_input)
            st.success(f"Image saved to: `{image_path}`")
            st.image(Image.open(image_path), caption=user_input, use_column_width=True)
        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.header("📸 Gallery")

def display_gallery():
    files = get_files()
    if not files:
        st.info("No images yet. Generate one above to start your gallery!")
        return
    cols = st.columns(3)
    for i, f in enumerate(files):
        col = cols[i % 3]
        img = Image.open(f["file_path"])
        col.image(img, caption=f["title"], use_column_width=True)

display_gallery()
