from PIL import Image
import pillow_heif
import pillow_avif
import tempfile
import streamlit as st

# Register HEIC/HEIF support
pillow_heif.register_heif_opener()


class ImageEngine:

    @staticmethod
    def normalize_format(fmt: str):
        """
        Normalize user format names to PIL formats.
        """
        fmt = fmt.upper()

        if fmt in ["JPG", "JFIF"]:
            return "JPEG"

        return fmt


    @staticmethod
    def convert_image(image_file, target_format):
        """
        Converts uploaded image to target format.
        Returns path of converted temp file.
        """

        try:
            fmt = ImageEngine.normalize_format(target_format)

            with Image.open(image_file) as img:

                img.load()

                # JPEG doesn't support transparency
                if fmt == "JPEG" and img.mode not in ["RGB"]:
                    img = img.convert("RGB")

                suffix = f".{target_format.lower()}"

                temp_output = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=suffix
                )

                output_path = temp_output.name
                temp_output.close()

                img.save(output_path, format=fmt)

                return output_path

        except Exception as e:
            st.error(f"Image conversion failed: {e}")
            return None


    @staticmethod
    def get_supported_formats():
        """
        Formats users can convert TO
        """
        return [
            "PNG",
            "JPEG",
            "JPG",
            "WEBP",
            "BMP",
            "TIFF",
            "AVIF"
        ]


    @staticmethod
    def get_supported_upload_types():
        """
        Formats users can upload.
        """
        return [
            "png",
            "jpg",
            "jpeg",
            "jfif",
            "webp",
            "bmp",
            "tiff",
            "heic",
            "heif",
            "avif"
        ]