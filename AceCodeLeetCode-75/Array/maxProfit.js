function maxProfit (prices) {
    let profit = 0;
    if (prices.length == 1) return profit;

    let left = 0;
    for (let right = left + 1; right < prices.length; right++) {
        if (prices[right] > prices[left]) {
            profit = Math.max(profit, prices[right] - prices[left]);
            // console.log(profit);
        } else {
            left = right;
        }
    }

    return profit;
}

console.log("I am answer ", maxProfit([7, 1, 5, 3, 6, 4]));