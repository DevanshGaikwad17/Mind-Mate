document.addEventListener("DOMContentLoaded", () => {
    const questions = document.querySelectorAll(".question");
    let currentStep = 0;
    const responses = {};

    // Function to show the current question and hide others
    function showQuestion(step) {
        questions.forEach((question, index) => {
            question.style.display = index === step ? "block" : "none";
        });
    }

    // Initialize with the first question
    showQuestion(currentStep);

    // Handle 'Next' button clicks
    document.querySelectorAll(".next-btn").forEach((button) => {
        button.addEventListener("click", () => {
            const questionElement = questions[currentStep];
            if (questionElement.querySelector("textarea")) {
                // Store textarea response
                responses[`q${currentStep + 1}`] = questionElement.querySelector("textarea").value;
            } else if (questionElement.querySelector("select")) {
                // Store select dropdown response
                responses[`q${currentStep + 1}`] = questionElement.querySelector("select").value;
            }
            
            if (currentStep < questions.length - 1) {
                currentStep++;
                showQuestion(currentStep);
            }
        });
    });

    // Handle form submission
    document.getElementById("surveyForm").addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent default form submission

        // Save responses to localStorage
        const surveyData = {
            date: new Date().toLocaleString(),
            responses: { ...responses }
        };
        const savedData = JSON.parse(localStorage.getItem("surveyResponses")) || [];
        savedData.push(surveyData);
        localStorage.setItem("surveyResponses", JSON.stringify(savedData));

        alert("Thank you for completing the survey!");

    });
});
