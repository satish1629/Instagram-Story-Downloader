
// Wait for the page to load before adding interactivity
document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const downloadButtons = document.querySelectorAll(".btn-success");
    
    // Form submission with loading animation
    form.addEventListener("submit", () => {
        const submitButton = form.querySelector("button");
        submitButton.textContent = "Loading...";
        submitButton.disabled = true;
    });

    // Add event listener to each download button
    downloadButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault();

            // Show download animation
            const originalText = button.textContent;
            button.textContent = "Downloading...";
            button.disabled = true;

            // Simulate download time
            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
            }, 2000);
        });
    });

    // Input validation for username
    const inputField = document.querySelector("input[name='username']");
    
    inputField.addEventListener("input", () => {
        const value = inputField.value.trim();
        const regex = /^(https?:\/\/)?(www\.)?instagram\.com\/[a-zA-Z0-9._]+\/?$/;

        if (regex.test(value) || /^[a-zA-Z0-9._]+$/.test(value)) {
            inputField.style.border = "2px solid #4caf50";  // Green for valid input
        } else {
            inputField.style.border = "2px solid #e91e63";  // Red for invalid input
        }
    });
});
