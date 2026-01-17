class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        # check if it is reachable
        # compare the quality if the quality is bigger then update the res

        res = [-1,-1]
        max_quality = float("-inf")
        centerX,centerY = center[0],center[1]
      
        for x,y,q in towers:
            # if it's reachable
            print( x,y,q )
            if abs(x-centerX)+abs(y-centerY)<= radius:
                #  reachable
                if q> max_quality or (q==max_quality and[x,y]<res):
                    max_quality =q
                    res=[x,y]
        

        return res 
            
                
        