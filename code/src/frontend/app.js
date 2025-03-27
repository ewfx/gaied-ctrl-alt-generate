document.getElementById('emailContentForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent traditional form submission

    const responseMessage = document.getElementById('responseMessage');

    // Get all uploaded files (email docs and attachments)
    const emailFiles = document.querySelectorAll('input[name="emailFiles[]"]');
    const attachmentFiles = document.querySelectorAll('input[name="attachmentFiles[]"]');

    if (!hasFiles(emailFiles) && !hasFiles(attachmentFiles)) {
        responseMessage.textContent = "Please upload at least one email document or attachment.";
        responseMessage.style.backgroundColor = "#f8d7da"; // Red background
        responseMessage.style.color = "#721c24"; // Dark red text
        return;
    }

    // Create a FormData object to send files to the backend
    let formData = new FormData();
    emailFiles.forEach(fileInput => {
        if (fileInput.files.length > 0) {
            formData.append("emailFiles", fileInput.files[0]);
        }
    });
    attachmentFiles.forEach(fileInput => {
        if (fileInput.files.length > 0) {
            formData.append("attachmentFiles", fileInput.files[0]);
        }
    });

    // Send the files to the backend (AI API) for analysis
    fetch('http://localhost:8000/analyze-email-content', { // Replace with your actual backend API endpoint
        method: 'POST',
        body: formData
    })
        .then(response => response.json())
        .then(data => {
            responseMessage.textContent = "Analysis Result: " + data.analysis; // Adjust based on your backend response
            responseMessage.style.backgroundColor = "#d4edda"; // Green background
            responseMessage.style.color = "#155724"; // Dark green text
        })
        .catch(error => {
            responseMessage.textContent = "Error: Unable to analyze the email content.";
            responseMessage.style.backgroundColor = "#f8d7da"; // Red background
            responseMessage.style.color = "#721c24"; // Dark red text
        });
});

// Function to check if at least one file is selected
function hasFiles(fileInputs) {
    for (let input of fileInputs) {
        if (input.files.length > 0) {
            return true;
        }
    }
    return false;
}

// Function to add a new file input field dynamically
function addFileInput(containerId) {
    let container = document.getElementById(containerId + "Container");
    let newInput = document.createElement("div");
    newInput.classList.add("file-upload");
    newInput.innerHTML = `
        <input type="file" name="${containerId}[]" accept=".txt,.pdf,.docx,.html">
        <button type="button" class="remove-file-btn" onclick="removeFileInput(this)">-</button>
    `;
    container.appendChild(newInput);
}

// Function to remove a file input field
function removeFileInput(button) {
    button.parentElement.remove();
}
