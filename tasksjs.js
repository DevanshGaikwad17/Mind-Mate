
let currentMonth = new Date().getMonth(); // Start with current month
let currentYear = new Date().getFullYear(); // Current year
let currentDate = `${currentYear}-${currentMonth + 1}-1`; // Default starting date

// Updates the selected date when clicked
function updateSelectedDate(date) {
    document.getElementById("selectedDate").innerText = `Selected Date: ${date}`;
    currentDate = date;  // Update the global selected date
    loadTasks();  // Load tasks for the selected date
}

// Function to load tasks from localStorage
function loadTasks() {
    const taskListDiv = document.getElementById("taskList");
    taskListDiv.innerHTML = "";  // Clear existing tasks

    tasks = JSON.parse(localStorage.getItem(currentDate)) || [];

    tasks.forEach((task, index) => {
        const taskItem = document.createElement("div");
        taskItem.className = "task-item";
        taskItem.innerHTML = `${task} <button onclick="deleteTask(${index})">Delete</button>`;
        taskListDiv.appendChild(taskItem);
    });
}

// Adds a task
function addTask() {
    const taskInput = document.getElementById("taskInput");
    const task = taskInput.value.trim();

    if (task) {
        tasks.push(task);  // Add task to the array
        taskInput.value = "";  // Clear input field
        saveTasks();  // Save updated tasks
        loadTasks();  // Refresh the task list
    }
}

// Deletes a task
function deleteTask(index) {
    tasks.splice(index, 1);  // Remove task from array
    saveTasks();  // Save updated tasks
    loadTasks();  // Refresh the task list
}

// Saves tasks to localStorage
function saveTasks() {
    localStorage.setItem(currentDate, JSON.stringify(tasks));
}

// Generates the calendar based on current month and year
function generateCalendar() {
    const calendarDiv = document.getElementById("calendar");
    const monthAndYear = document.getElementById("monthAndYear");

    monthAndYear.innerText = `${new Date(currentYear, currentMonth).toLocaleString('default', { month: 'long' })} ${currentYear}`;

    calendarDiv.innerHTML = "";  // Clear the calendar before populating

    const firstDay = new Date(currentYear, currentMonth).getDay();  // Get the first day of the month
    const daysInMonth = new Date(currentYear, currentMonth + 1, 0).getDate();  // Get the number of days in the month

    // Create empty divs to fill days before the first day
    for (let i = 0; i < firstDay; i++) {
        const emptyDiv = document.createElement("div");
        emptyDiv.className = "day";
        calendarDiv.appendChild(emptyDiv);
    }

    // Create divs for each day of the month
    for (let i = 1; i <= daysInMonth; i++) {
        const dayDiv = document.createElement("div");
        dayDiv.className = "day";
        dayDiv.innerText = i;
        dayDiv.addEventListener("click", () => updateSelectedDate(`${currentYear}-${currentMonth + 1}-${i}`));
        calendarDiv.appendChild(dayDiv);
    }
}

// Initialize the calendar
generateCalendar();

// Navigation to the previous and next month
document.getElementById("prevMonth").addEventListener("click", () => {
    currentMonth = currentMonth === 0 ? 11 : currentMonth - 1;
    currentYear = currentMonth === 11 ? currentYear - 1 : currentYear;
    generateCalendar();
});

document.getElementById("nextMonth").addEventListener("click", () => {
    currentMonth = currentMonth === 11 ? 0 : currentMonth + 1;
    currentYear = currentMonth === 0 ? currentYear + 1 : currentYear;
    generateCalendar();
});
