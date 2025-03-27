import docx
from email import message_from_binary_file
import extract_msg
import pypdf
from fastapi import UploadFile

def extract_msg_from_file(file: UploadFile) -> str:
    """
    Extract text content from a file based on its format.

    Args:
        file (UploadFile): The uploaded file to extract text from.

    Returns:
        str: The extracted text content.

    Raises:
        ValueError: If the file format is unsupported.
        RuntimeError: If an error occurs during text extraction.
    """
    file_format = file.filename.split(".")[-1]
    extractors = {
        "eml": extract_text_from_eml,
        "msg": extract_text_from_msg,
        "pdf": extract_text_from_pdf,
        "docx": extract_text_from_docx,
    }
    try:
        if file_format not in extractors:
            raise ValueError("Unsupported file format. Please upload a .eml, .msg, .pdf, or .docx file.")
        file_body = extractors[file_format](file.file)
    except Exception as e:
        raise RuntimeError(f"Error extracting text from file: {e}")
    return file_body

def extract_text_from_eml(eml_file) -> str:
    """
    Extract text content from an .eml email file.

    Args:
        eml_file: The file object of the .eml email.

    Returns:
        str: The extracted plain text content of the email.
    """
    msg = message_from_binary_file(eml_file)

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            # Prefer plain text parts.
            if content_type == "text/plain":
                part_payload = part.get_payload(decode=True)
                if part_payload:
                    body += part_payload.decode(errors='ignore')
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode(errors='ignore')

    return body

def extract_text_from_msg(msg_path) -> str:
    """
    Extract text content from a .msg email file.

    Args:
        msg_path: The file path or file object of the .msg email.

    Returns:
        str: The extracted plain text content of the email.
    """
    msg = extract_msg.Message(msg_path)
    return msg.body

def extract_text_from_pdf(pdf_path) -> str:
    """
    Extract text content from a PDF file.

    Args:
        pdf_path: The file path or file object of the PDF.

    Returns:
        str: The extracted text content of the PDF.
    """
    text = ""
    with open(pdf_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def extract_text_from_docx(doc_path) -> str:
    """
    Extract text content from a Word document.

    Args:
        doc_path: The file path or file object of the Word document.

    Returns:
        str: The extracted text content of the Word document.
    """
    doc = docx.Document(doc_path)
    return "\n".join([para.text for para in doc.paragraphs])

