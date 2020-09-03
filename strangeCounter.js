// function strangeCounter(t) {
//     let col = 3;
//     let count = 3;
//     for (let i = 0; i < t; i++) {
//         if (count === 0) {
//             col *= 2;
//             count = col;
//         }
//         count -= 1;
//     }


//     return count + 1;

// }


// const strangeCounter = (t) => {
//     let col = 3;
//     let counter = 3;
//     const count = (ticks) => {
//         console.log(col)
//         console.log(counter)
//         if (ticks === 0) { return counter }
//         if (counter === 0) {
//             col *= 2;
//             counter = col;
//         }
//         counter--;

//         count(ticks - 1)
//     }

//     count(t)
// }


// const strangeCounter = (t) => {
//     let value = 3;

//     while (t > value) {
//         t = t - value;
//         value *= 2;
//     }


//     return (value - t + 1)
// }



// const strangeCounter = (t) => {
//     let value = 3;
//     let col = 3;

//     while (t > value) {
//         col *= 2;
//         value += col;
//         // console.log('total slots presented:', value)
//         // console.log('final col header:', col)
//     }



//     for (let i = 0; i < col; i--) {
//         if (value === t) { return (-i + 1) }
//         value--;
//     }
// }

const strangeCounter = (t) => {

    let value = 3
    while (t > value) {
        t -= value;
        value *= 2;
    }

    console.log('Whats left of t:', t)
    console.log('Col value:', value)

    return (value - t + 1)
}



console.log(strangeCounter(4));