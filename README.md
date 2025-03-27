# 🚀 MailGuard

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
In the Commercial Bank Lending Service domain, teams receive a high volume of diverse email requests, often with attachments, requiring manual triage by "Gatekeepers" to classify and extract key information. This manual process is not only time-consuming and inefficient but also prone to errors, especially as the volume of requests increases.  

To address this challenge, our project leverages **Generative AI** to develop an intelligent solution that automates **email classification and context-based data extraction**. By integrating AI-driven automation, we aim to significantly improve efficiency, accuracy, and turnaround time—reducing manual effort while ensuring precise request handling.  

This solution will streamline operations, minimize errors, and enhance productivity, enabling lending service teams to focus on higher-value tasks rather than manual triage. 🚀

## 🎥 Demo 
📹 [Video Demo](#)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
The inspiration for this project came from the challenges faced by Commercial Bank Lending Service teams, who deal with an overwhelming number of email requests daily. These emails often include attachments and require manual triage by "Gatekeepers" to classify, extract key information, and route service requests appropriately.

This manual process is:

📌 Time-consuming – Processing large volumes of emails manually slows down operations.

📌 Error-prone – Human oversight can lead to misclassification, missed information, or incorrect routing.

📌 Inefficient – Valuable time is spent sorting and extracting data instead of focusing on higher-value tasks.

To solve these issues, we are developing a Gen AI-powered solution that automates email classification and context-based data extraction. By reducing manual effort and enhancing accuracy, this system improves operational efficiency, minimizes errors, and accelerates turnaround time, ensuring that service requests are processed more effectively.

## ⚙️ What It Does
This project is an AI-powered email classification and automation system designed for Commercial Bank Lending Service teams. It leverages Generative AI to automate email triage, extract key information, and reducing manual effort and improving efficiency.

By eliminating error-prone and time-consuming manual processing, this solution ensures faster turnaround times, accurate request handling, and enhanced operational efficiency for banking service teams.

Key Features & Functionalities

📌 Automated Email Classification
Uses GenAI to analyze email content and categorize requests into predefined service types.

Identifies urgency and priority levels to ensure faster processing of critical emails.

📌 Context-Based Data Extraction
Extracts key details (e.g., loan amounts, account numbers, customer names, and document types) from emails and attachments.

Uses Natural Language Processing (NLP) to understand unstructured email text and extract relevant information.

📌 Attachment Analysis & Processing
Supports multiple file formats (EML, MSG, DOCX, PDF) and extracts crucial details from them.

Uses AI-powered document parsing to identify and extract structured data from unstructured attachments.

📌 Enhanced Accuracy & Efficiency
Minimizes human errors in classification.

Speeds up processing time by automating repetitive tasks that previously required manual intervention.

📌 User-Friendly Interface
Simple file upload system for emails and attachments.

Provides real-time analysis results with intuitive feedback.

## 🛠️ How We Built It
To develop our GenAI-powered Email Classification and Automation System, we leveraged a combination of cutting-edge AI models and efficient web technologies to ensure seamless automation, accuracy, and scalability.

Technologies, Frameworks & Tools Used:

1️⃣ GenAI & Natural Language Processing (NLP)

Gemini API – Used for intelligent email classification and context-aware data extraction.

LangChain – To orchestrate AI models and integrate with business workflows.

2️⃣ Backend & API Development

Python (FastAPI) – To build a robust and scalable backend API for processing emails and attachments.

## 🚧 Challenges We Faced
During the development of our GenAI-powered Email Classification, our team encountered several technical and non-technical challenges:

1️⃣ Handling Diverse Email Formats and Attachments

🔹 Challenge: Emails arrive in various formats (plain text, PDFs, Word documents, EML, etc.), making consistent classification and data extraction difficult.

🔹 Solution: We implemented multi-format parsing using Natural Language Processing (NLP)

2️⃣ Context-Aware Classification & Extraction

🔹 Challenge: Extracting meaningful insights from unstructured emails while ensuring contextual understanding was complex.

🔹 Solution: Leveraged Large Language Models (LLMs) to analyze email context, detect intent, and extract relevant fields dynamically.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/ewfx/gaied-ctrl-alt-generate.git
   ```
2. Install dependencies  
   ```sh
   pip install -r code/src/backend/requirements.txt (for Python)
   ```
3. Start the server
   ```sh
   cd code/src/backend
   uvicorn main:app --reload
   ```

## 🏗️ Tech Stack
- Backend: Python (FastAPI)
- GenAI/ NLP: Gemini API

## 👥 Team
- **Ahana Vishwakarma** - [GitHub](https://github.com/ahanavish) | [LinkedIn](https://www.linkedin.com/in/ahanavish/)
- **Nithin Raj K M** - [GitHub](https://github.com/nithinrajkm) | [LinkedIn](https://www.linkedin.com/in/nithinrajkm/)
- **Rutu Shrirame** - [GitHub](https://github.com/rutu1012) | [LinkedIn](https://www.linkedin.com/in/rutushrirame/)
- **Saikishore Kothakota** - [LinkedIn](https://www.linkedin.com/in/saikishore-kothakota-3637ab83/)
- **Sri Hari Krishnan** - [GitHub](https://github.com/Sri1263) | [LinkedIn](https://www.linkedin.com/in/sri-hari-krishnan/)
