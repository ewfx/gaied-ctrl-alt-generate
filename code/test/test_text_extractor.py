import pytest
from fastapi import UploadFile
from io import BytesIO
from modules.text_extractor import extract_msg_from_file

@pytest.fixture
def mock_eml_file():
    content = b"Subject: Test Email\n\nThis is a test email."
    return UploadFile(filename="test.eml", file=BytesIO(content))

@pytest.fixture
def mock_msg_file():
    # Mock content for a .msg file
    content = b"Mock MSG content"
    return UploadFile(filename="test.msg", file=BytesIO(content))

@pytest.fixture
def mock_pdf_file():
    # Mock content for a PDF file
    content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog >>\nendobj\n"
    return UploadFile(filename="test.pdf", file=BytesIO(content))

@pytest.fixture
def mock_docx_file():
    # Mock content for a .docx file
    content = b"PK\x03\x04Mock DOCX content"
    return UploadFile(filename="test.docx", file=BytesIO(content))

def test_extract_eml(mock_eml_file):
    result = extract_msg_from_file(mock_eml_file)
    assert "This is a test email." in result

def test_extract_msg(mock_msg_file):
    with pytest.raises(RuntimeError):
        extract_msg_from_file(mock_msg_file)

def test_extract_pdf(mock_pdf_file):
    with pytest.raises(RuntimeError):
        extract_msg_from_file(mock_pdf_file)

def test_extract_docx(mock_docx_file):
    with pytest.raises(RuntimeError):
        extract_msg_from_file(mock_docx_file)

def test_unsupported_file_format():
    unsupported_file = UploadFile(filename="test.txt", file=BytesIO(b"Unsupported content"))
    with pytest.raises(ValueError, match="Unsupported file format"):
        extract_msg_from_file(unsupported_file)
