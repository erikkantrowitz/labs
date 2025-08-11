function ticketPrice(age) {
    if (age < 13) return 8;
    if (age >= 13 && age <= 64) return 12;
    if (age >= 65) return 10;
    else return 'input not given as a number';
}

console.log(ticketPrice(8));   // expect: 8
console.log(ticketPrice(18));  // expect: 12
console.log(ticketPrice(64));  // expect: 12
console.log(ticketPrice(65));  // expect: 10
console.log(ticketPrice("b"));  // expect: else string