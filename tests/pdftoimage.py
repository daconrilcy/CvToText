import fitz  # PyMuPDF
from PIL import Image
import tesserocr

# Ouvrir le PDF
pdf_document = "ProfileLinkedin.pdf"
doc = fitz.open(pdf_document)

# Itérer sur les pages
for page_number in range(doc.page_count):
    page = doc.load_page(page_number)
    pix = page.get_pixmap(dpi=144)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    # Utiliser tesserocr sur l'image
    text = tesserocr.image_to_text(img)
    print(f"Texte de la page {page_number + 1}:\n{text}")

print("***************************Conversion terminée*********************************")

imagedocument = "Cv_test.jpg"
with tesserocr.PyTessBaseAPI() as api:
    api.SetImageFile(imagedocument)
    text = api.GetUTF8Text()
    print(f"Texte de la page :\n{text}")