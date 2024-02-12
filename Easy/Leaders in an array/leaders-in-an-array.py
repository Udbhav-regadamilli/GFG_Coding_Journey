class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        ans = []
        max_right = A[N - 1]
    
        # The last element is always a leader
        ans.append(max_right)
    
        # Traverse the array from right to left
        for i in range(N - 2, -1, -1):
            if A[i] >= max_right:
                max_right = A[i]
                ans.append(max_right)
    
        # Reverse the leaders found to maintain the original order
        ans.reverse()
        return ans






#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends