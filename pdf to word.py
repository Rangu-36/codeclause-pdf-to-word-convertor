from pdfminer.high_level import extract_text
from docx import Document

def sanitize_text(text):
    # Remove characters not compatible with XML formatting
    sanitized_text = "".join(c if c.isprintable() else " " for c in text)
    return sanitized_text

def pdf_to_word(pdf_file, docx_file):
    # Extract the text from the PDF
    text = extract_text(pdf_file)
    
    # Sanitize the extracted text
    sanitized_text = sanitize_text(text)
    
    # Create a new Word document
    document = Document()
    
    # Add the sanitized text to the Word document
    document.add_paragraph(sanitized_text)
    
    # Save the Word document to the specified path
    document.save(docx_file)

# Example usage
pdf_to_word('C:/Users/sushma/Downloads/project1/rangu.pdf', 'C:/Users/sushma/Downloads/worddocx.docx')
