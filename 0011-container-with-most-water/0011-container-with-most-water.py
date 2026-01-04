class Solution:
    def maxArea(self, height: List[int]) -> int:
      # maxArea
        # l and r to record the wall
        # calculate the Heights is the minimum of l and r
        # calculate the Area is the maximum of height and the l-r+1
    
        maxArea = float("-inf")
        l,r = 0,len(height)-1
        while l < r:
            width = r-l
            h = min(height[l],height[r])
            maxArea=max(maxArea, width*h)
            

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea
          