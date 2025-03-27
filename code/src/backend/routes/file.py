from typing import Annotated
from fastapi import APIRouter, File, UploadFile, HTTPException
from controllers.file_handler import handle_mail_upload, handle_mail_upload_with_attachments

router = APIRouter()

@router.post("/singlemail/", description="Upload a single file")
def upload_mail(mail_file: Annotated[UploadFile, File(description="The file to upload")]):
    """
    Upload a single email
    """
    try:
        response = handle_mail_upload(mail_file)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    return response

@router.post("/mailwithattachments/", description="Upload multiple files")
def upload_mail_with_attachments(mails: Annotated[list[UploadFile], File(description="Upload one or more Mails as .eml or .msg")], attachments: Annotated[list[UploadFile], File(description="Upload one or more Attachments of format .docx or .pdf")]):
    """
    Upload email and attachments
    """
    try:
        response = handle_mail_upload_with_attachments(mails, attachments)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {e}")
    return response

