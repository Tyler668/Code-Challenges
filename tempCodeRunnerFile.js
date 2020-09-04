
    // const getPillarSurfaceArea = (y, x) => {
    //     let SA = 0;
    //     const heightOfPillar = board[y][x];
    //     let adjacents = assessNeighbors(y, x);

    //     let padding = 8 - adjacents.length;

    //     for (let i = 0; i < padding; i++) {
    //         adjacents.push(0);
    //     }

    //     for (let i = 0; i < adjacents.length; i++) {
    //         if (adjacents[i] < heightOfPillar) {
    //             SA += (heightOfPillar - adjacents[i]);
    //         }
    //     }

    //     return SA + 1;
    // }

    // console.log(getPillarSurfaceArea(0, 0))