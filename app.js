function navigateTo(pageId) {
    document.querySelectorAll('.page').forEach(page => page.classList.add('hidden'));
    document.getElementById(pageId).classList.remove('hidden');
}

// Simulate user data storage
let userData = {};

// Sign-Up Function
function signUp(event) {
    event.preventDefault();
    const email = document.getElementById('signUpEmail').value;
    const gender = document.getElementById('signUpGender').value;
    const age = document.getElementById('signUpAge').value;
    const occupation = document.getElementById('signUpOccupation').value;

    userData = { email, gender, age, occupation };

    alert("Sign Up Successful!");
    navigateTo('signInPage');
}

// Log-In Function
function signIn(event) {
    event.preventDefault();
    const email = document.getElementById('loginEmail').value;

    // Basic validation check
    if (userData.email === email) {
        alert("Login Successful!");
        navigateTo('homePage');
        displayProfile();
    } else {
        alert("Incorrect email. Please sign up first.");
    }
}

// Display user profile data
function displayProfile() {
    document.getElementById('profileEmail').innerText = userData.email;
    document.getElementById('profileGender').innerText = userData.gender;
    document.getElementById('profileAge').innerText = userData.age;
    document.getElementById('profileOccupation').innerText = userData.occupation;
}


// Handle Chat Form Submission
async function handleChat(event) {
    event.preventDefault();

    const chatInput = document.getElementById("chatInput");
    const chatDisplay = document.getElementById("chatDisplay");
    const userMessage = chatInput.value;

    // Display user's message
    chatDisplay.innerHTML += `<p><strong>You:</strong> ${userMessage}</p>`;
    chatInput.value = ""; // Clear input field

    // Get prediction from the model
    const response = await fetch("http://localhost:5000/chat-predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ input_text: userMessage }),
    });

    const result = await response.json();
    const botResponse = result.output; // Return the model's output text

    // Display the bot's response
    chatDisplay.innerHTML += `<p><strong>Bot:</strong> ${botResponse}</p>`;

    // Scroll to the latest message
    chatDisplay.scrollTop = chatDisplay.scrollHeight;
}


async function handleHealth(event) {
    event.preventDefault();
    const data = {
        gender: parseInt(document.getElementById("reportGender").value),
        age: parseInt(document.getElementById("reportAge").value),
        occupation: parseInt(document.getElementById("reportOccupation").value),
        sleep_duration: parseFloat(document.getElementById("reportSleep_Duration").value),
        quality_sleep: parseInt(document.getElementById("reportquality_sleep").value),
        activity_level: parseFloat(document.getElementById("reportPhysical_Activity_Level").value),
        stress_level: parseInt(document.getElementById("reportStress_Level").value),
        bmi: parseInt(document.getElementById("reportBMI_Catogery").value),
        heart_rate: parseInt(document.getElementById("reportHeart_rate").value),
        steps: parseInt(document.getElementById("reportSteps").value),
        sleep_disorder: parseInt(document.getElementById("reportSleep_Disorder").value),
        bp_high: parseInt(document.getElementById("reportBP_High").value),
        bp_low: parseInt(document.getElementById("reportBP_Low").value)
    };
    try {
        // Send data to the Flask API
        const response = await fetch("http://localhost:5000/health-predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        // Check if the response is okay
        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }

        // Parse JSON response
        const result = await response.json();

        // Display the output from the server
        alert("From you reports it seems that you are " + result.output);

    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
    }
}
