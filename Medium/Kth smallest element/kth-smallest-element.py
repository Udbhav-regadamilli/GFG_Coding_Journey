#User function Template for python3

class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        # Implementing QuickSort
        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        # Finding the Kth smallest element using QuickSelect algorithm
        def quickSelect(arr, l, r, k):
            if k > 0 and k <= r - l + 1:
                pivot = partition(arr, l, r)
                if pivot - l == k - 1:
                    return arr[pivot]
                elif pivot - l > k - 1:
                    return quickSelect(arr, l, pivot - 1, k)
                else:
                    return quickSelect(arr, pivot + 1, r, k - pivot + l - 1)
            return float('inf')
        
        return quickSelect(arr, l, r, k)



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends