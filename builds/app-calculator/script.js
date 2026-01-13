<!--
// Calculator script
//
// Author: Interface & Interaction Engineer
//
// Description:
//   This script implements a complete calculator functionality.
//   It includes display update functions, event listeners for all buttons,
//   calculation logic for all operations (addition, subtraction, multiplication, division),
//   decimal point handling, clear function, and equals function to evaluate and show result.
//
// Dependencies:
//   None
//
// Usage:
//   This script is designed to work independently without requiring any external libraries or dependencies.
//
// Notes:
//   All logic should be fully functional.
//
--> 
const display = document.getElementById('display');
const buttons = document.querySelectorAll('button);

buttons.forEach(button => {
  button.addEventListener('click', () => {
    const value = button.textContent;

    if (value === 'C') {
      display.value = '';
    } else if (value === '=') {
      try {
        display.value = eval(display.value);
      } catch (error) {
        display.value = 'Error';
      }
    } else {
      display.value += value;
    }
  });
});