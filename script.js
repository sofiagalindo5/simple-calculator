let display = document.getElementById("display");

// Add characters to the display
function press(key) {
  display.value += key;
}

// Calculate the result when '=' is clicked
function calculate() {
  try {
    display.value = eval(display.value);
  } catch (error) {
    display.value = "Error";
  }
}

// Clear the display (for 'C' button)
function clearDisplay() {
  display.value = "";
}