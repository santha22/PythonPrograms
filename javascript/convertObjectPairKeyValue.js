const ArrData = (arr) => {
    return Object.fromEntries(arr);
}
console.log(ArrData([
    ['a', 1],
    ['b', 2],
    ['c', 3],
    ['d', 4],
]));