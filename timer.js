// Timer countdown functionality
let timerElement = document.getElementById('timer');
let timeLeft = 300;

function updateTimer() {
  let minutes = Math.floor(timeLeft / 60);
  let seconds = timeLeft % 60;
  seconds = seconds < 10 ? '0' + seconds : seconds;
  timerElement.textContent = `${minutes}:${seconds}`;
  
  if (timeLeft > 0) {
    timeLeft--;
    setTimeout(updateTimer, 1000);
  }
}

updateTimer(); // Start the timer
