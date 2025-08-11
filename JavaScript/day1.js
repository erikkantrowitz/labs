const myName = "Erik";
let counter = 0;

function greeting (name) {
    console.log("hello, " + name);
}

function increment(counter) {
    return counter + 1;
}

greeting(myName);

console.log(increment(counter));
console.log(counter);

function average(a,b) {
    // //check if inputs are numbers
    // if(typeof(a) == isFinite && typeof(b) === isFinite)
        return (a + b) / 2;

}

console.log(average(3,4));
console.log(average(3,"4"));

function returnLength(word) {
    return word.length;
}
console.log("hi is " + returnLength("hi") + " letters");