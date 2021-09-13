function getTotalScore(nums) {
    let score = 0;
    for (let n of nums) {
        if (n == 5) score += 5;
        else if (n % 2 == 0) score += 1;
        else score += 3;
    }
    return score;    
}

print(getTotalStore([1,2,3,4,5]));