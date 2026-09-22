class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        map1 = {}
        map2 = {}
        i1 = l
        i2 = r
        h1 = height[l]
        h2 = height[r]
        if len(height) >1:
            while height[l+1]>=height[l] :
                if l+1< len(height) - 1:
                    l += 1
            while height[r-1]>=height[r] and r>1:
                if r-1 >0:
                    r -= 1
        while l<r:
            
            if height[l+1]<height[l]:
                i1 = l
                h1 = height[i1]
                map1[i1] = h1

            if height[r-1]<height[r]:
                i2 = r
                h2 = height[i2]
                map2[i2] = h2
            while l<r and height[l]<=height[r]:
                while (l+1<r and height[l+1]<h1 and height[l]<=h1) or (l+1<r and height[l+1]>=h1 and height[l+1]>=height[l]):
                    l += 1
                if l+1<r and height[l]>=h1 and height[l+1]<=height[l]:
                    i1 = l
                    h1 = height[i1]
                    map1[i1] = h1
                    
                elif l+1==r:
                    l += 1
                    break
                

            while l<r and height[l]>height[r]:
                while (l<r-1 and height[r-1]<h2 and height[r]<=h2) or (l<r-1 and height[r-1]>=h2 and height[r-1]>=height[r]):
                    r -= 1
                if l<r-1 and height[r]>=h2 and height[r-1]<=height[r]:
                    i2 = r
                    h2 = height[i2]
                    map2[i2] = h2
            

                elif l==r-1:
                    r -= 1
                    break

        map = map1 | dict(reversed(map2.items()))
    
        lst = list(map.keys())
        if map == {}:
            return 0
        area = 0
        for i in range(len(lst)-1):
            area += min(map[lst[i]], map[lst[i+1]])* (lst[i+1]-lst[i]-1) - sum(min(x, min(map[lst[i]], map[lst[i+1]])) for x in height[lst[i]+1 : lst[i+1]])
        return area