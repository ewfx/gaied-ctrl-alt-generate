# Backend Source Code Directory

This directory contains the backend source code for the project. Below is an overview of the key components and their purpose.

---

## 📂 Modules
### `text_extractor.py`
- **Purpose**: Provides utility functions to extract text from various file formats.
- **Supported Formats**:
  - `.eml`: Extracts plain text from email files.
  - `.msg`: Extracts plain text from Outlook message files.
  - `.pdf`: Extracts text from PDF documents.
  - `.docx`: Extracts text from Word documents.
- **Key Functions**:
  - `extract_msg_from_file`: Determines the file type and delegates extraction to the appropriate function.
  - `extract_text_from_eml`: Handles `.eml` files.
  - `extract_text_from_msg`: Handles `.msg` files.
  - `extract_text_from_pdf`: Handles `.pdf` files.
  - `extract_text_from_docx`: Handles `.docx` files.

---

## 📂 Controllers
### `file_handler.py`
- **Purpose**: Manages the processing of uploaded files and their attachments.
- **Key Functions**:
  - `handle_mail_upload`: Processes a single email file and extracts its content.
  - `handle_mail_upload_with_attachments`: Processes multiple email files and their attachments, then sends the combined content to the LLM client for classification and extraction.

---

## 📂 Routes
### `base.py`
- **Purpose**: Defines the root endpoint of the API.
- **Endpoints**:
  - `GET /`: Returns a simple "Hello World" message.

### `text.py`
- **Purpose**: Handles text-based API requests.
- **Endpoints**:
  - `POST /text`: Accepts a text payload and returns a mock response with a confidence score.

### `file.py`
- **Purpose**: Handles file upload API requests.
- **Endpoints**:
  - `POST /uploadfile/`: Accepts a single file upload and processes it.
  - `POST /uploadfiles/`: Accepts multiple files and attachments, processes them, and returns the LLM client response.

---

## 📂 Config
### `prompt_config.py`
- **Purpose**: Contains the prompt used by the LLM client for processing email content.
- **Details**:
  - The prompt is designed to classify emails as either inquiries or loan requests.
  - For loan requests, it extracts details such as request type, sub-request type, and loan amount.

---

## How to Run
1. **Install Dependencies**:
   Ensure all required dependencies are installed. Use the following command:
   ```sh
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   Start the FastAPI application using:
   ```sh
   uvicorn main:app --reload
   ```

3. **Access API Documentation**:
   Open your browser and navigate to:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Backend Structure
```
backend/
├── config/
│   ├── __init__.py
│   ├── prompt_config.py
├── controllers/
│   ├── file_handler.py
├── modules/
│   ├── __init__.py
│   ├── llm_connector.py
│   ├── text_extractor.py
├── routes/
│   ├── base.py
│   ├── file.py
│   ├── text.py
├── main.py
```

---

## Notes
- **Environment Variables**:
  - Ensure the `.env` file contains the required `GOOGLE_API_KEY` for the LLM client.
- **Error Handling**:
  - The application uses FastAPI's `HTTPException` for error handling.
