def knapsack(val,wt,w,n) :
    if n==0 or w==0 :
        return 0
    if wt[n-1] > w :
        return knapsack(val,wt,w,n-1)
    else :
        return max(val[n-1]+knapsack(val,wt,w-wt[n-1],n-1), knapsack(val,wt,w,n-1))


val = [60,100,120] 
wt = [10,20,40]  
w = 50 
n = len(val)
print('maximum profit = ',knapsack(val,wt,w,n))
