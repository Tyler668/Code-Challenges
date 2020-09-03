function isSet(cards) {
    let colors = []
    let numbers = []
    let shades = []
    let shapes = []

    let attrs = [colors, numbers, shades, shapes]

    for (let i = 0; i < cards.length; i++) {
        colors.push(cards[i].color);
        numbers.push(cards[i].number);
        shades.push(cards[i].shade);
        shapes.push(cards[i].shape);
    }

    console.log(attrs)


    for (let i = 0; i < attrs.length; i++) {
        if (attrs[i][0] === attrs[i][1] === attrs[i][2]) {
            continue
        }
        else if (attrs[i][0] != attrs[i][1] && attrs[i][0] != attrs[i][2] && attrs[i][1] != attrs[i][2]) {
            continue
        }
        else {
            return false
        }
    }
    return true

}



console.log(isSet(
    [{ color: "red", number: 1, shade: "lined", shape: "squiggle" },
    { color: "red", number: 1, shade: "lined", shape: "squiggle" },
    { color: "red", number: 1, shade: "lined", shape: "squiggle" }]
))







    //     if (cards[i].color === cards[i + 1].color === cards[i + 2].color) {
    //         allSame = true
    //     }
    //     else if (cards[i.color] != cards[i + 1].color != cards[i + 2].color) {
    //         allDifferent = true
    //     }
    //     else {
    //         return false
    //     }

    //     if (cards[i].color === cards[i + 1].color === cards[i + 2].color) {
    //         allSame = true
    //     }
    //     else if (cards[i.color] != cards[i + 1].color != cards[i + 2].color) {
    //         allDifferent = true
    //     }
    //     else {
    //         return false
    //     }


    //     if (cards[i].color === cards[i + 1].color === cards[i + 2].color) {
    //         allSame = true
    //     }
    //     else if (cards[i.color] != cards[i + 1].color != cards[i + 2].color) {
    //         allDifferent = true
    //     }
    //     else {
    //         return false
    //     }


    //     if (cards[i].color === cards[i + 1].color === cards[i + 2].color) {
    //         allSame = true
    //     }
    //     else if (cards[i.color] != cards[i + 1].color != cards[i + 2].color) {
    //         allDifferent = true
    //     }
    //     else {
    //         return false
    //     }

    // }
