import pytest
from fastapi import UploadFile, HTTPException
from io import BytesIO
from src.controllers.file_handler import handle_mail_upload, handle_mail_upload_with_attachments

@pytest.fixture
def mock_mail_file():
    content = b"Subject: Test Email\n\nThis is a test email."
    return UploadFile(filename="test.eml", file=BytesIO(content))

@pytest.fixture
def mock_attachment_file():
    content = b"Attachment content"
    return UploadFile(filename="attachment.pdf", file=BytesIO(content))

def test_handle_mail_upload(mock_mail_file):
    result = handle_mail_upload(mock_mail_file)
    assert "content" in result
    assert "This is a test email." in result["content"]

def test_handle_mail_upload_with_attachments(mock_mail_file, mock_attachment_file):
    result = handle_mail_upload_with_attachments([mock_mail_file], [mock_attachment_file])
    assert "response" in result
    # Add more assertions based on the expected response structure

def test_handle_mail_upload_invalid_file():
    invalid_file = UploadFile(filename="test.txt", file=BytesIO(b"Invalid content"))
    with pytest.raises(HTTPException):
        handle_mail_upload(invalid_file)
