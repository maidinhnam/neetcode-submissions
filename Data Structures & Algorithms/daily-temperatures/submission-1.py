class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        slack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while slack!= [] and temperatures[i] > temperatures[slack[-1]]:
                res[slack[-1]] = i - slack[-1]
                slack.pop()
            slack.append(i)
        return res