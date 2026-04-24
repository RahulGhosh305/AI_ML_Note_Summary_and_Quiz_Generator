import streamlit as st

# Header Section
st.title("Note Summary & Quiz Generator", anchor=False)
st.markdown("Upload 3 images to generate a summary and quiz based on the content of the images.")
st.divider()

# Sidebar for image upload
with st.sidebar:
    st.header("Upload Images")
    uploaded_images = st.file_uploader(
        "Choose images",
        accept_multiple_files=True,
        type=["jpg", "jpeg", "png"],
        key="image_upload"
    )

    # Display uploaded images
    if uploaded_images:
        st.subheader("Uploaded Images")
        if len(uploaded_images) > 3:
            st.error("Please upload only 3 images.")
        else:
            col = st.columns(len(uploaded_images))
            for i, image in enumerate(uploaded_images):
                with col[i]:
                    st.image(image, caption=image.name, output_format="auto")

    # Difficulty level selection
    st.header("Quiz Difficulty Level")
    selected_difficulty = st.selectbox(
        "Select difficulty level",
        options=["Easy", "Medium", "Hard"],
        key="difficulty",
        index=None
    )

    # Button
    pressed = st.button("Create Summary & Quiz Generator", key="create_button", type="primary")

# Main Content
if pressed:
    if not uploaded_images:
        st.error("You must upload at least 1 image.")
    elif not selected_difficulty:
        st.error("You must select a difficulty level.")
    else:
        # Note
        with st.container(border=True):
            st.subheader("Image Summary", anchor=False)
            st.text("This note comes from gemini api")

        # Audio Transcript
        with st.container(border=True):
            st.subheader("Audio Transcription", anchor=False)
            st.text("This note comes from gemini api")

        # Quiz Generate
        with st.container(border=True):
            st.subheader(f"Your {selected_difficulty} Quiz", anchor=False)
            st.text("This note comes from gemini api")