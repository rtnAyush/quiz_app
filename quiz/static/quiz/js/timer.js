document.addEventListener("DOMContentLoaded", function () {
    var countdownValue = 15;  // Set the countdown to 15 seconds
    var countdownElement = document.getElementById("countdown");  // 

    function updateCountdown() {
        countdownElement.innerText = countdownValue;  // Display the countdown value
        countdownValue--;  // Decrease the countdown value by 1 every second

        if (countdownValue < 0) {  // When the countdown reaches 0
            clearInterval(countdownInterval);  // Stop the countdown
            countdownElement.style.color = "red"
            // countdownElement.innerText = "Time's up!";  // Display a "Time's up!" message
            // You can add additional logic here to redirect or submit the form, etc.
        }
    }

    // Update the countdown every second (1000ms = 1 second)
    var countdownInterval = setInterval(updateCountdown, 1000);
});


function isClicked(element) {
    // Get all elements with the class 'option'
    var allEles = document.getElementsByClassName('option');

    // Remove the 'clicked' class from all elements
    for (let ele of allEles) {
        ele.classList.remove("clicked");
    }

    // Add the 'clicked' class to the clicked element
    element.classList.add('clicked');
}