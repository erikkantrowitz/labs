// Make a const city = "Chicago" and const temp = 72.
// Log "Today in Chicago it is 72°F." using a template literal.
// Make a const items = 5 and const pricePerItem = 10.
// Log "Your total is $50" using ${items * pricePerItem} inside the string.
// Try a multiline quote with at least one ${} expression in it.

const city = "Chicago";
const temp = 72;
console.log(`Today in ${city} it is ${temp}°F.`);

const items = 50;
const pricePerItem = 2;
console.log(`Your total is $${items * pricePerItem}`);

console.log(`A trip to
    ${city} is
    $${items * pricePerItem}`);
