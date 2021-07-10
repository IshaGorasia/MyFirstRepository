def makingCoinChange(coin,amt) :
    table = [0 for i in range(amt+1)]
    table[0] = 1
    for i in range(len(coin))  :
        for j in range(coin[i],amt+1) :
            table[j] += table[j-coin[i]]
    return table[amt]

coin = [2,3,5,10]
amt = 15
print('Total no of possible combinations = ',makingCoinChange(coin,amt))
