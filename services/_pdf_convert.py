import fitz  # PyMuPDF
from PIL import Image
from services._image_convert import image_to_text


def pdf_to_text(pdf_path):
    text_final = ""
    try:
        # Ouvrir le PDF
        doc = fitz.open(pdf_path)
        # Itérer sur les pages
        for page_number in range(doc.page_count):
            page = doc.load_page(page_number)
            pix = page.get_pixmap(dpi=144)
            img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            # Utiliser tesserocr sur l'image
            text = image_to_text(img)
            text_final += text
        return text_final
    except Exception as e:
        print(f"Erreur lors de la conversion du PDF en image: {e}")
        return ''