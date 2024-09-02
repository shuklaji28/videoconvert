import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

def convert_to_mp4(input_file_path):
    """Converts the uploaded video file to MP4 format."""
    try:
        # Load the video file clip from the file path
        video = VideoFileClip(input_file_path)
        
        # Create a temporary file path for the output MP4 file
        output_temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        output_file_path = output_temp_file.name

        # Write the video to the output file in MP4 format
        video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

        return output_file_path
    except Exception as e:
        st.error(f"Error converting file: {e}")
        return None

# Initialize the Streamlit app
st.title("Video Converter: WMV to MP4")
st.write("Upload a video file in WMV format or any other supported format to convert it to MP4.")

# File upload
uploaded_file = st.file_uploader("Choose a video file", type=["wmv", "avi", "mov", "mkv", "flv"])

if uploaded_file is not None:
    # Display file details
    st.write("File uploaded successfully!")
    st.video(uploaded_file)

    # Convert the uploaded file to MP4
    if st.button("Convert to MP4"):
        with st.spinner('Converting...'):
            # Save the uploaded file to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wmv") as temp_input_file:
                temp_input_file.write(uploaded_file.read())
                temp_input_path = temp_input_file.name

            # Convert the video
            output_file_path = convert_to_mp4(temp_input_path)

            # Remove the temporary input file
            os.remove(temp_input_path)

            if output_file_path:
                # Provide a download button for the converted MP4 file
                st.success("Conversion successful!")
                with open(output_file_path, "rb") as file:
                    st.download_button(label="Download MP4", data=file, file_name="converted_video.mp4", mime="video/mp4")
                
                # Remove the temporary output file
                os.remove(output_file_path)
