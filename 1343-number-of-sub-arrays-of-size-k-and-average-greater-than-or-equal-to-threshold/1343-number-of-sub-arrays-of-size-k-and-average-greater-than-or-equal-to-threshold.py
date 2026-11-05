class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        # calculate the first window 
        #  left side out and right side go into the window
        #  check if the average is bigger or equal to threshold
        #  return the number
        sum_win=sum(arr[:k])
        target = threshold * k
        count= 1 if sum_win >= target else 0

        for r in range(k,len(arr)):
            sum_win+= arr[r]-arr[r-k]
            if sum_win >= target:
                count +=1

        return count
        