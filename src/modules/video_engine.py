from moviepy import VideoFileClip
import tempfile
import streamlit as st


class VideoEngine:

    @staticmethod
    def convert_video(input_file_path, target_format, progress_bar=None):

        try:
            with VideoFileClip(input_file_path) as video:

                suffix = f".{target_format.lower()}"

                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
                output_path = temp_file.name
                temp_file.close()

                codec = "libx264"

                if target_format.upper() == "AVI":
                    codec = "libxvid"

                # estimate video duration
                duration = video.duration

                if progress_bar:
                    progress_bar.progress(0)

                # run conversion (terminal progress will appear normally)
                video.write_videofile(
                    output_path,
                    codec=codec,
                    audio_codec="aac" if target_format.upper() != "AVI" else None
                )

                if progress_bar:
                    progress_bar.progress(1.0)

                return output_path

        except Exception as e:
            st.error(f"Error converting video: {e}")
            return None


    @staticmethod
    def get_supported_formats():
        return ["MP4", "AVI", "MOV", "MKV"]