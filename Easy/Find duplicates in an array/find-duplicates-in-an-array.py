class Solution:
    
    def duplicates(self, arr, n): 
    	dic = {}
    	ans = []
    	
    	for i in arr:
    	    if i in dic:
    	       ans.append(i)
    	    else:
    	        dic[i] = 1
    	       
    	ans = list(set(ans))
    	ans.sort()
    	        
        return ans if ans else [-1]
    	       
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends