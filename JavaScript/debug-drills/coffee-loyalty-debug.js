function loyaltyBonus(isMember, drinksPurchased) {
    if (isMember && drinksPurchased >= 10) {
        return "Free coffee!";
    }
    return "No reward yet";
}

console.log(loyaltyBonus(true, 12));  // expect: "Free coffee!"
console.log(loyaltyBonus(false, 12)); // expect: "No reward yet"