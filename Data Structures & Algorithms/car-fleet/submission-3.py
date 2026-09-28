class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        group = {}
        res = 1
        for i in range(len(position)):
            group[position[i]] = (target + speed[i] - position[i] )/ speed[i]
        count = 0
        for j in reversed(sorted(group)):
            if count == 0:
                c = group[j]
                count += 1
            if group[j] > c:
                res += 1
                c = group[j]
        return res