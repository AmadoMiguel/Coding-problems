function getNTribonacciNums(triboSeries:number[],n:number) {
    if (n <= 3) return triboSeries.slice(0, n);
    let currIdx = 2;
    for (let i = 4; i <= n; i++) {
        let nextTriboNum = triboSeries[currIdx] + triboSeries[currIdx-1]+triboSeries[currIdx-2];
        triboSeries.push(nextTriboNum);
        currIdx += 1;
    }
    return triboSeries;
}

console.log(getNTribonacciNums([0,0,1],9));