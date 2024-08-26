# dispatch.py
# The dispactcher function takes two arguments: filename and file_path.
from services._csv_reader import csv_reader
from services._json_reader import json_file_reader
from services._text_reader import text_reader
from services._pdf_convert import pdf_to_text
from services._image_convert import image_to_text


def dispatcher(filename, file_path):
    if filename.endswith('.txt'):
        return text_reader(file_path)
    elif filename.endswith('.csv'):
        return csv_reader(file_path)
    elif filename.endswith('.json'):
        return json_file_reader(file_path)
    elif filename.endswith('.pdf'):
        return pdf_to_text(file_path)
    elif filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        return image_to_text(file_path)
    else:
        raise ValueError('Unknown file type')