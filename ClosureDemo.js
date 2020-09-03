var count = () => {
    let counter = 0;

    return increment = () => {
        return counter++;
    }

}



// count()
// console.log(count()())
// console.log(count()())
// console.log(count()())
// console.log(count()())



// let X = count()

// console.log(X())
// console.log(X())
// console.log(X())
// console.log(X())

//-------------------------------------------------------------

outer = () => {
    var secret = "It's all a simulation"


    return inner = () => {
        // superSecret = secret
        console.log("The truth is; " + secret)
    }
}







outer()

// console.log(secret)s


let V = outer()
V()

