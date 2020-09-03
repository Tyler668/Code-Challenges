const strangeCounter = (t) => {
    let value = 3;

    while (t > value) {
        t = t - value;
        value *= 2;
    }


    return (value - t + 1)
}
