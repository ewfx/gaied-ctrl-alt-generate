from fastapi import UploadFile, HTTPException
from modules.text_extractor import extract_msg_from_file
from modules import llm_client  # Import the initialized LLM client

def handle_mail_upload(mail_file: UploadFile) -> dict[str, str]:
    """
    Handle the upload of a single email file.

    Args:
        mail_file (UploadFile): The uploaded email file.

    Returns:
        dict[str, str]: A dictionary containing the extracted content of the email.

    Raises:
        HTTPException: If an error occurs during file processing.
    """
    try:
        file_body = extract_msg_from_file(mail_file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing mail file: {e}")

    return {"content": file_body}

def handle_mail_upload_with_attachments(mails: list[UploadFile], attachments: list[UploadFile]) -> dict[str, dict]:
    """
    Handle the upload of multiple email files and their attachments.

    Args:
        mails (list[UploadFile]): A list of uploaded email files.
        attachments (list[UploadFile]): A list of uploaded attachment files.

    Returns:
        dict[str, dict]: A dictionary containing the response from the LLM client.

    Raises:
        HTTPException: If an error occurs during file or attachment processing.
    """
    try:
        message = "MAIL CONTENT: "
        for mail in mails:
            message += extract_msg_from_file(mail)

        message += "\n\nATTACHMENTS: "
        for attachment in attachments:
            message += "\n" + extract_msg_from_file(attachment)

        response = llm_client.classify_email_and_extract_details(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing mail and attachments: {e}")

    return {"response": response}

