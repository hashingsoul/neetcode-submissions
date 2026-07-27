class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        x=2
        for i in range(x):
            for n in nums:
                ans.append(n)
        return ans