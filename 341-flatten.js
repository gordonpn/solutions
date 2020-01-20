// Write a function to flatten an array in optimal time.
// Example: 
// let input = [1, [2, [ [3, 4], 5], 6]];
// flatten(input); //[1, 2, 3, 4, 5, 6]

function flatten(input) {
    let flatInput = []
    
    input.forEach(item => {
        let temp = flatten_helper(item);
        if (Array.isArray(temp)) {
            flatInput = flatInput.concat(temp)
        } else {
            flatInput.push(temp)
        }
    });
    return flatInput;
}

function flatten_helper(input) {
    if (Array.isArray(input)) {
        return flatten(input)
    } else {
        return input
    }
}

// let input = [1, [2, 3]]
let input = [1, [2, [ [3, 4], 5], 6]];
console.log(flatten(input));