
def printknapSack(W, wt, val, n): 
	K = [[0 for w in range(W + 1)] 
			for i in range(n + 1)] 
			
 
	for i in range(n + 1): 
		for w in range(W + 1): 
			if i == 0 or w == 0: 
				K[i][w] = 0
			elif wt[i - 1] <= w: 
				K[i][w] = max(val[i - 1] 
				+ K[i - 1][w - wt[i - 1]], 
							K[i - 1][w]) 
			else: 
				K[i][w] = K[i - 1][w] 

	res = K[n][W] 
	print(res) 
	
	w = W 
	for i in range(n, 0, -1): 
		if res <= 0: 
			break 
		if res == K[i - 1][w]: 
			continue
		else: 

			
			print ("Selected :")
			print(val[i - 1]) 
		 
			res = res - val[i - 1] 
			w = w - wt[i - 1] 
 
val = [1,2,3,4] 
wt = [2, 5, 6, 8] 
W = 17
n = 4
	
printknapSack(W, wt, val, n) 

