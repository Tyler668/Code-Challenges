// const potentialNeighbors = [board[y - 1][x - 1], board[y - 1][x], board[y - 1][x + 1], board[y][x - 1], board[y][x + 1], board[y + 1][x - 1], board[y + 1][x], board[y + 1][x + 1]];


function surfaceArea(A) {
    let columns = A[0][0];
    let rows = A[0][1];
    let boardArea = columns * rows;
    let toyPrice = 0;

    const board = [];

    for (let i = 1; i < A.length; i++) {
        board.push(A[i]);
    }

    // console.log(board)

    const assessNeighbors = (y, x) => {
        let neighbors = [];

        for (let i = 0; i < columns; i++) {
            for (let j = 0; j < rows; j++) {
                if ((Math.abs((y - i)) <= 1 && x === j) || (Math.abs(x - j) <= 1 && y === i)) {
                    if (y != i || x != j) {
                        neighbors.push(board[i][j])
                    }
                }
            }
        }
        return neighbors;
    }

    // console.log('N:', assessNeighbors(0, 0))

    const getPillarSurfaceArea = (y, x) => {
        let SA = 0;
        let heightOfPillar = board[y][x];
        let adjacents = assessNeighbors(y, x);

        let padding = 4 - adjacents.length;

        if (padding != 0) {
            for (let i = 0; i < padding; i++) {
                adjacents.push(0);
            }
        }


        for (let i = 0; i < adjacents.length; i++) {
            if (adjacents[i] < heightOfPillar) {
                SA += (heightOfPillar - adjacents[i]);
            }
        }

        return SA + 2;
    }

    // console.log('Pillar SA:', getPillarSurfaceArea(2, 1))



    for (let i = 0; i < columns; i++) {
        for (let j = 0; j < rows; j++) {
            toyPrice += getPillarSurfaceArea(i, j);
        }
    }


    console.log(toyPrice);
    return toyPrice;
}




let A = [
    [4, 4],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [2, 4, 6, 8],
    [1, 3, 5, 7]
]


let A2 = [
    [1, 1],
    [100]
]


let A3 = [
    [3, 3],
    [1, 3, 4],
    [2, 2, 3],
    [1, 2, 4]
]

console.log(surfaceArea(A2)); 