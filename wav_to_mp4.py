# -----------MODULAR CODE -------------------------
import streamlit as st
from moviepy.editor import VideoFileClip
import tempfile
import os

class VideoConverterApp:
    def __init__(self):
        self.setup_ui()

    def setup_ui(self):
        """Initialize the Streamlit app UI."""
        # Add custom CSS for styling
        st.markdown(self.custom_css(), unsafe_allow_html=True)

        with st.container():
            st.markdown("<div class='main'><h1 class='stTitle'>Video Converter: WMV to MP4</h1>", unsafe_allow_html=True)
            st.divider()
            st.markdown(self.subtitle(), unsafe_allow_html=True)
            st.divider()

            # File upload
            uploaded_file = st.file_uploader("Choose a video file", type=["wmv", "avi", "mov", "mkv", "flv"])
            if uploaded_file:
                self.display_uploaded_file(uploaded_file)
                self.handle_conversion(uploaded_file)

    def custom_css(self):
        """Return custom CSS for the app."""
        return """
            <style>
            .main {
                background-color: #f0f0f5;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            }
            .stButton>button {
                color: white;
                background-color: #4CAF50;
                border-radius: 5px;
                padding: 10px 20px;
            }
            .stDownloadButton>button {
                color: white;
                background-color: #FF6347;
                border-radius: 5px;
                padding: 10px 20px;
            }
            .stTitle {
                color: #4CAF50;
                font-size: 40px;
                font-weight: bold;
                text-align: center;
                margin-bottom: 0px;
            }
            .stSubtitle {
                color: #333;
                font-size: 20px;
                text-align: center;
                margin-bottom: 0px;
            }
            </style>
        """

    def subtitle(self):
        """Return the subtitle HTML with a hyperlink."""
        return """
            <h3 class='stSubtitle'>
                Hi, <a href='https://linkedin.com/in/shresthshuklaji' style='color: #FF6347; text-decoration: none;'>Shresth</a> this side. 
                Just created this quick application to convert your videos into MP4 format. 
                Upload a video file in WMV format or any other supported format to convert it to MP4. 
                Video might not be visible on the interface, so directly click convert button once uploaded.
            </h3>
        """

    def display_uploaded_file(self, uploaded_file):
        """Display the uploaded video file."""
        st.write("### File uploaded successfully!")
        st.video(uploaded_file)

    def handle_conversion(self, uploaded_file):
        """Handle the conversion of the uploaded file."""
        if st.button("Convert to MP4"):
            with st.spinner('Converting...'):
                temp_input_path = self.save_uploaded_file(uploaded_file)
                output_file_path = self.convert_to_mp4(temp_input_path)
                os.remove(temp_input_path)

                if output_file_path:
                    self.display_download_button(output_file_path)

    def save_uploaded_file(self, uploaded_file):
        """Save the uploaded file to a temporary location and return the file path."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wmv") as temp_input_file:
            temp_input_file.write(uploaded_file.read())
            return temp_input_file.name

    def convert_to_mp4(self, input_file_path):
        """Convert the video file to MP4 format."""
        try:
            video = VideoFileClip(input_file_path)
            output_temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            output_file_path = output_temp_file.name
            video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")
            return output_file_path
        except Exception as e:
            st.error(f"Error converting file: {e}")
            return None

    def display_download_button(self, output_file_path):
        """Display the download button for the converted file."""
        st.success("Conversion successful!")
        with open(output_file_path, "rb") as file:
            st.download_button(label="Download MP4", data=file, file_name="converted_video.mp4", mime="video/mp4")
        os.remove(output_file_path)

if __name__ == "__main__":
    VideoConverterApp()

# ----- PREVIOUS CODE -----------
# import streamlit as st
# from moviepy.editor import VideoFileClip
# import tempfile
# import os

# def convert_to_mp4(input_file_path):
#     """Converts the uploaded video file to MP4 format."""
#     try:
#         # Load the video file clip from the file path
#         video = VideoFileClip(input_file_path)
        
#         # Create a temporary file path for the output MP4 file
#         output_temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
#         output_file_path = output_temp_file.name

#         # Write the video to the output file in MP4 format
#         video.write_videofile(output_file_path, codec="libx264", audio_codec="aac")

#         return output_file_path
#     except Exception as e:
#         st.error(f"Error converting file: {e}")
#         return None

# # Initialize the Streamlit app
# # st.title("Video Converter: WMV to MP4")
# # st.write("Upload a video file in WMV format or any other supported format to convert it to MP4.")



# # Adding custom CSS for styling
# st.markdown(
#     """
#     <style>
#     .main {
#         background-color: #f0f0f5;
#         padding: 20px;
#         border-radius: 10px;
#         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     }
#     .stButton>button {
#         color: white;
#         background-color: #4CAF50;
#         border-radius: 5px;
#         padding: 10px 20px;
#     }
#     .stDownloadButton>button {
#         color: white;
#         background-color: #FF6347;
#         border-radius: 5px;
#         padding: 10px 20px;
#     }
#     .stTitle {
#         color: #4CAF50;
#         font-size: 40px;
#         font-weight: bold;
#         text-align: center;
#         margin-bottom: 0px;
#     }
#     .stSubtitle {
#         color: #333;
#         font-size: 20px;
#         text-align: center;
#         margin-bottom: 0px;
#     }
#     </style>
#     """, unsafe_allow_html=True
# )


# with st.container(border=True):
#     # Initialize the Streamlit app with a title and subtitle
#     st.markdown("<div class='main'><h1 class='stTitle'>Video Converter: WMV to MP4</h1>", unsafe_allow_html=True)
    
#     st.divider()
    
#     st.markdown("""
#     <h3 class='stSubtitle'>
#         Hi, <a href='https://linkedin.com/in/shresthshuklaji' style='color: #FF6347; text-decoration: none;'>Shresth</a> this side. Just created this quick application to convert your videos into MP4 format. 
#         Upload a video file in WMV format or any other supported format to convert it to MP4. Video might not be visible on the interface, so directly click convert button once uploaded.
#     </h3>
#     """, unsafe_allow_html=True)
#     st.divider()
    
    
#     # File upload
#     uploaded_file = st.file_uploader("Choose a video file", type=["wmv", "avi", "mov", "mkv", "flv"])
    
#     if uploaded_file is not None:
#         # Display file details
#         st.write("### File uploaded successfully!")
#         st.video(uploaded_file)
    
#         # Convert the uploaded file to MP4
#         if st.button("Convert to MP4"):
#             with st.spinner('Converting...'):
#                 # Save the uploaded file to a temporary file
#                 with tempfile.NamedTemporaryFile(delete=False, suffix=".wmv") as temp_input_file:
#                     temp_input_file.write(uploaded_file.read())
#                     temp_input_path = temp_input_file.name
    
#                 # Convert the video
#                 output_file_path = convert_to_mp4(temp_input_path)
    
#                 # Remove the temporary input file
#                 os.remove(temp_input_path)
    
#                 if output_file_path:
#                     # Provide a download button for the converted MP4 file
#                     st.success("Conversion successful!")
#                     with open(output_file_path, "rb") as file:
#                         st.download_button(label="Download MP4", data=file, file_name="converted_video.mp4", mime="video/mp4")
                    
#                     # Remove the temporary output file
#                     os.remove(output_file_path)

