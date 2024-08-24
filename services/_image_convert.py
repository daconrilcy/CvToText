from tesserocr import PyTessBaseAPI


def image_to_text(file_path):
    try:
        with PyTessBaseAPI() as api:
            api.SetImageFile(file_path)
            text = api.GetUTF8Text()
        return text
    except Exception as e:
        print(f"Exception: {e}")
        return ''