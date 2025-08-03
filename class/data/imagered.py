import os
from docx import Document
from PIL import Image
import pytesseract
from io import BytesIO

def extract_images_and_ocr(docx_path):
    doc = Document(docx_path)
    rels = doc.part.rels
    all_texts = []

    for rel in rels:
        rel = rels[rel]
        if "image" in rel.target_ref:
            image_data = rel.target_part.blob
            image_stream = BytesIO(image_data)
            img = Image.open(image_stream)

            # OCR on the image
            text = pytesseract.image_to_string(img)
            all_texts.append(text.strip())

    return all_texts

def save_texts_to_file(texts, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        for i, text in enumerate(texts, 1):
            f.write(f"Text from image {i}:\n")
            f.write(text + "\n")
            f.write("-" * 40 + "\n")

if __name__ == "__main__":
    docx_path = "Nepal Pharma new11.docx"  # replace with your .docx file path
    output_file = "output1.txt"    # output file name

    extracted_texts = extract_images_and_ocr(docx_path)
    save_texts_to_file(extracted_texts, output_file)

    print(f"Extracted text saved to {output_file}")
