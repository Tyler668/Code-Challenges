function repeatedString(s, n) {
    let aCount = 0;
    let additionalA = 0;

    for (let i = 0; i < s.length; i++) {
        if (s[i] === 'a') { aCount++; }
    }

    let remainder = n % s.length;

    for (let i = 0; i < remainder; i++) {
        if (s[i] === 'a') { additionalA++; }
    }



    aCount = ((n - remainder) / s.length) * aCount + additionalA;

    // if (s === 'a') {
    //     return n;
    // }

    // s = s.split('')



    // for (let i = 0; i < n; i++) {
    //     let index = i % s.length;
    //     if (s[index] === 'a') {
    //         aCount++;
    //     }
    // }
    return aCount;
}

console.log(repeatedString('aba', 10));