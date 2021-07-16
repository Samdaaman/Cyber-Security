// function without parameters
function addTwoNumbers() {
    var numOne = 10;
    var numTwo = 20;
    var sum = numOne + numTwo;
}
addTwoNumbers(); // function has to be called to be executed
// Function without parater doesn' take input, so lets make a parameter with parameter
function sumTwoNumbers(numOne, numTwo) {
    var sum = numOne + numTwo;
}
sumTwoNumbers(10, 20); // calling functions
// If a function doesn't return it doesn't store data, so it should return
function sumTwoNumbersAndReturn(numOne, numTwo) {
    var sum = numOne + numTwo;
    return sum;
}
function printFullName(firstName, lastName) {
    return `${firstName} ${lastName}`;
}

function square(number) {
    return number * number;
}

// this function takes array as a parameter and sum up the numbers in the array
function sumArrayValues(arr) {
    var sum = 0;
    for (var i = 0; i < arr.length; i++) {
        sum = sum + numbers[i];
    }
    return sum;
}
const numbers = [1, 2, 3, 4, 5];

//
function sumOfEvensAndOdds() {
    var sumOfEvens = 0;
    var sumOfOdds = 0;
    for (var i = 0; i <= 100; i++) {
        if (i % 2 === 0) {
            sumOfEvens = sumOfEvens + i;
        } else {
            sumOfOdds = sumOfOdds + i;
        }
    }
    return { evens: sumOfEvens, odds: sumOfOdds };
    //return [sumOfEvens, sumOfOdds];
    //return `The sum of all evens is ${sumOfEvens}. And the sum of all odds is ${sumOfOdds}`;
}