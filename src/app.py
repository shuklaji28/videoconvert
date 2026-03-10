import streamlit as st
import os
import tempfile
from modules.video_engine import VideoEngine
from modules.image_engine import ImageEngine

st.set_page_config(
    page_title="Media Converter",
    page_icon="🎬",
    layout="centered"
)

# ---------------- CSS ---------------- #
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background: linear-gradient(135deg,#eef2ff,#ffffff);
}

/* Title */
.title {
    font-size: 3rem;
    font-weight: 700;
    text-align:center;
    background: linear-gradient(90deg,#6366F1,#8B5CF6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle{
    text-align:center;
    color:#6b7280;
    margin-bottom:30px;
}

/* Card */
.card {
    background:white;
    padding:25px;
    border-radius:16px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.05);
    margin-bottom:20px;
}

/* Buttons */
.stButton>button {
    width:100%;
    border-radius:10px;
    height:45px;
    font-weight:600;
    background:linear-gradient(90deg,#6366F1,#8B5CF6);
    color:white;
    border:none;
}

.stButton>button:hover{
    transform:scale(1.02);
}

/* Footer */
.footer{
    text-align:center;
    color:#6b7280;
    margin-top:40px;
    font-size:0.9rem;
}

.footer a{
    text-decoration:none;
    color:#6366F1;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-testid="stFileUploader"]{
    border:2px dashed #6366F1;
    border-radius:12px;
    padding:15px;
    background:#f9fafb;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("<div class='title'>🎬 Media Converter</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Convert videos and images instantly — fast, simple and secure</div>",
    unsafe_allow_html=True
)

tab1, tab2 = st.tabs(["🎥 Video Converter", "🖼 Image Converter"])

# ---------------- VIDEO TAB ---------------- #

with tab1:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns([3,1])

    with col1:
        uploaded_videos = st.file_uploader(
            "Upload videos",
            type=["wmv","avi","mov","mkv","flv","mp4"],
            accept_multiple_files=True
        )

    with col2:
        target_format = st.selectbox(
            "Convert To",
            VideoEngine.get_supported_formats()
        )

    if uploaded_videos:

        st.success(f"{len(uploaded_videos)} videos ready")

        if st.button("Convert Videos 🚀"):

            for idx, video_file in enumerate(uploaded_videos):

                status = st.empty()
                status.info(f"Converting {video_file.name}...")

                progress_bar = st.progress(0)

                suffix = f".{video_file.name.split('.')[-1]}"

                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as t:
                    t.write(video_file.read())
                    temp_path = t.name

                output_path = VideoEngine.convert_video(
                    temp_path,
                    target_format,
                    progress_bar
                )

                os.remove(temp_path)

                if output_path:

                    status.success(f"{video_file.name} converted!")

                    with open(output_path, "rb") as f:

                        st.download_button(
                            "Download Converted Video",
                            f,
                            file_name=f"{os.path.splitext(video_file.name)[0]}.{target_format.lower()}",
                            mime=f"video/{target_format.lower()}",
                            key=f"vid_{idx}"
                        )

                    os.remove(output_path)

                else:
                    status.error("Conversion failed")
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- IMAGE TAB ---------------- #

with tab2:

    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns([3,1])

    with col1:
        uploaded_images = st.file_uploader(
            "Upload images",
            type=ImageEngine.get_supported_upload_types(),
            accept_multiple_files=True
        )

    with col2:
        target_format = st.selectbox(
            "Convert To",
            ImageEngine.get_supported_formats(),
            index=1
        )

    if uploaded_images:

        st.success(f"{len(uploaded_images)} images ready")

        if st.button("Convert Images 🚀"):

            cols = st.columns(2)

            for idx, img in enumerate(uploaded_images):

                with cols[idx % 2]:

                    st.image(img)

                    output_path = ImageEngine.convert_image(img, target_format)

                    if output_path:

                        with open(output_path,"rb") as f:

                            st.download_button(
                                "Download",
                                f,
                                file_name=f"{os.path.splitext(img.name)[0]}.{target_format.lower()}",
                                mime=f"image/{target_format.lower()}",
                                key=f"img_{idx}"
                            )

                        os.remove(output_path)

                    else:
                        st.error("Failed")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #

st.markdown("""
<div class='footer'>
Built with ❤️ by <a href="https://linkedin.com/in/shresthshuklaji">Shresth</a> |
Blog: <a href="https://uselessai.in">uselessai.in</a>
</div>
""", unsafe_allow_html=True)