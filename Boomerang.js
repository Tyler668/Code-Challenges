function countBoomerangs(arr) {
    var boomerCount = 0
    for (i = 0; i < arr.length; i++) {
        if (arr[i] === arr[i + 2] && arr[i] != arr[i + 1]) {
            boomerCount++
        }
    }
    return boomerCount
}



console.log(countBoomerangs([1, 2, 1, 3, 4, 3, 6, 3]))