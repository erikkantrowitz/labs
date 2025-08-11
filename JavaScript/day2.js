// Movie Ticket Price
// Create a program that:
// Has a variable for age.
// If under 13 → child price: $8.
// If 13 to 64 → adult price: $12.
// If 65 or older → senior price: $10.
// Log the correct message including the price.

function ticketPrice(age) {
    if (age < 13) return 8;
    if (age >=13 && age < 64) return 12;
    else return 10;
}

console.log(`The ticket price for an 8 year old is $${ticketPrice(8)}`);
console.log(`The ticket price for an 18 year old is $${ticketPrice(18)}`);
console.log(`The ticket price for an 82 year old is $${ticketPrice(82)}`);

// Coffee Shop Loyalty Bonus
// Have two variables: isMember (true/false) and drinksPurchased (number).
// If a member and they’ve purchased at least 10 drinks, log "Free coffee!".
// Otherwise log "No reward yet".

function loyaltyBonus(isMember, drinksPurchased) {
    if(isMember && drinksPurchased >=10) return "Free Coffee";
    else return "No current reward";
}

console.log(`Thank you for your purchase: ${loyaltyBonus(true,10)}`);
console.log(`Thank you for your purchase: ${loyaltyBonus(false,10)}`);
console.log(`Thank you for your purchase: ${loyaltyBonus(true,3)}`);
console.log(`Thank you for your purchase: ${loyaltyBonus(false,30)}`);

// Login Attempt
// Have two variables: username and password.
// If both match your “stored” credentials, log "Login successful".
// If username matches but password doesn’t, log "Wrong password".
// Otherwise log "User not found".

const username = "testuser";
const password = "testuser";

function passwordCheck(username, password) {
    if (username === "testuser" && password === "testuser") return "login successful";
    if (username === "testuser" && password !== "testuser") return "Wrong password";
    else return "User not found";
}

console.log(`Logging in
    ...
    ...
    ${passwordCheck("testuser", "testuser")}`);

console.log(`Logging in
    ...
    ...
    ${passwordCheck("testuser", "Blah")}`);

console.log(`Logging in
    ...
    ...
    ${passwordCheck("blah", "gublah")}`);

console.log(`Logging in
    ...
    ...
    ${passwordCheck("blah", "testuser")}`);


// Speeding Ticket
// Have a variable for speed.
// If speed is greater than 70 and less than 90, log "Minor speeding".
// If speed is 90 or above, log "Major speeding" and "License suspended" on a separate line.
// Otherwise log "All good".

function speedingTicket(speed) {
    if (speed > 70 && speed < 90) return "Minor speeding";
    if (speed > 90) return `major speeding
License suspened`
    else return "All good";
}

console.log(speedingTicket(82));
console.log(speedingTicket(122));
console.log(speedingTicket(62));

// Ternary Challenge
// Have a variable points.
// If points >= 100, set status to "Gold"; otherwise set it to "Silver".
// Log: "Membership level: <status>" using interpolation.

function ternaryChallenge(points) {
    //condition ? expression_if_true : expression_if_false;
    return points >= 100 ? "gold" : "silver";
}

console.log(ternaryChallenge(33));
console.log(ternaryChallenge(313));
console.log(ternaryChallenge(100));