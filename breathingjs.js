document.getElementById("startButton").addEventListener("click", function() {
  let time = 30;
  const timerElement = document.getElementById("timer");

  const interval = setInterval(() => {
    const minutes = String(Math.floor(time / 60)).padStart(2, '0');
    const seconds = String(time % 60).padStart(2, '0');
    timerElement.textContent = `${minutes}:${seconds}`;

    if (time === 0) {
      clearInterval(interval);
      alert("Breathing exercise completed!");
    } else {
      time--;
    }
  }, 1000);
});
