// app.js

document.getElementById('emailContentForm').addEventListener('submit', function (e) {
    e.preventDefault();  // Prevent the form from submitting the traditional way

    const emailContent = document.getElementById('emailContent').value;
    const responseMessage = document.getElementById('responseMessage');

    if (emailContent.trim() === "") {
        responseMessage.textContent = "Please enter the email content to analyze.";
        responseMessage.style.backgroundColor = "#f8d7da";  // Red background
        responseMessage.style.color = "#721c24";  // Dark red text
        return;
    }

    // Send the email content to the backend (AI API) for analysis
    fetch('http://localhost:8000/analyze-email-content', {  // Replace with your actual backend API endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ content: emailContent })
    })
        .then(response => response.json())
        .then(data => {
            // Display the AI analysis response
            responseMessage.textContent = "Analysis Result: " + data.analysis;  // Adjust based on your backend response
            responseMessage.style.backgroundColor = "#d4edda";  // Green background
            responseMessage.style.color = "#155724";  // Dark green text
        })
        .catch(error => {
            responseMessage.textContent = "Error: Unable to analyze the email content.";
            responseMessage.style.backgroundColor = "#f8d7da";  // Red background
            responseMessage.style.color = "#721c24";  // Dark red text
        });
});


// Function to add a new file input field dynamically
function addFileInput() {
    const fileInputsContainer = document.getElementById("fileInputs");
    const currentInput = fileInputsContainer.lastElementChild.querySelector("input");

    // Check if the current file input has a file selected
    if (currentInput.files.length > 0) {
        // Create a new file input container
        const newFileInputContainer = document.createElement("div");
        newFileInputContainer.classList.add("file-input-container");

        // Create a new file input element
        const newFileInput = document.createElement("input");
        newFileInput.type = "file";
        newFileInput.name = "emailFiles[]";
        newFileInput.accept = ".txt,.pdf,.docx,.html";
        newFileInput.required = true;

        // Create a new "+" button
        const newAddButton = document.createElement("span");
        newAddButton.classList.add("add-file-btn");
        newAddButton.textContent = "+";
        newAddButton.onclick = addFileInput; // Attach the addFileInput function to the new "+" button

        // Append the new file input and "+" button to the container
        newFileInputContainer.appendChild(newFileInput);
        newFileInputContainer.appendChild(newAddButton);

        // Append the new container to the file inputs section
        fileInputsContainer.appendChild(newFileInputContainer);
    } else {
        alert("Please select a file before adding a new input.");
    }
}
