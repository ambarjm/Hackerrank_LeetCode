def maxArea(self, height):
        maxarea=0
        left ,right =0,len(height)-1
        while left< right:
           area=(right-left)*min(height[left],height[right])
           maxarea=max(area,maxarea)
           if height[left] < height[right]:
                left=left+1
           else:
               right=right-1

        return(maxarea)
