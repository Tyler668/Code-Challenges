// function rotLeft(a, d) {


//     return newArr;
// }

function rotLeft(a, d) {
    for (let i = 0; i < d; i++) {
        let first = a.shift();
        a.push(first);
    }
    return a;
}

console.log(rotLeft([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7));

// let arr = [1, 2, 3, 4]
// console.log(arr);
// arr[1] = 1;
// console.log(arr);