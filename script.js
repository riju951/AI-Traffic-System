let textToDisplay = "Hi! we are Tromso...";
let index = 0;
let animatedTextElement = document.getElementById("animated-text");

function typeText() {
    if (index < textToDisplay.length) {
        animatedTextElement.textContent += textToDisplay.charAt(index);
        index++;
        setTimeout(typeText, 150);  // Adjust the typing speed here. Lower value = faster typing
    }
}

typeText();

// Simulated traffic data for demonstration
const trafficData = {
    lane1: 30, // Number of vehicles in lane 1
    lane2: 45, // Number of vehicles in lane 2
    // Add more lanes as needed
};

// Function to update traffic data and visualize it
function updateTrafficData() {
    // Fetch real data using OpenCV or another method
    // For demonstration purposes, we'll use simulated data
    // Replace this with actual OpenCV integration
    // ...

    // Update the dashboard with the new data
    document.getElementById('lane1').innerText = trafficData.lane1;
    document.getElementById('lane2').innerText = trafficData.lane2;
    // Update more lanes if necessary
}

// Call the updateTrafficData function periodically (e.g., every few seconds)
setInterval(updateTrafficData, 5000); // Update every 5 seconds

// Simulated dynamic traffic light timings
const trafficLightTimings = {
    greenTime: 30, // Green light duration in seconds
    // Add more timings for other lights if necessary
};

// Function to update traffic light timings
function updateTrafficLightTimings() {
    // Calculate and update traffic light timings based on real-time data
    // Replace this with actual neural network predictions
    // ...

    // Update the dashboard with the new timings
    document.getElementById('greenTime').innerText = trafficLightTimings.greenTime;
    // Update timings for other lights if necessary
}

// Call the updateTrafficLightTimings function periodically
setInterval(updateTrafficLightTimings, 10000); // Update every 10 seconds
