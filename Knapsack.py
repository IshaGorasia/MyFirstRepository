#knapsack using DP
def knapsack(val,wt,W,n) :
    if n==0 or W == 0 :
        return 0
    if (wt[n-1] > W) : 
        return knapsack(val,wt,W,n-1)
    else :
        return max(val[n-1]+knapsack(val,wt,W-wt[n-1],n-1),knapsack(val,wt,W,n-1))

val = [60,100,120] 
wt = [10,20,40]   
w = 50 
n = len(val)
print('maximum profit = ',knapsack(val,wt,w,n))
