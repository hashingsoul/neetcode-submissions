class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap value:index
        hash={}
        for i,n in enumerate(nums):#index,number
            find=target-n
            if find in hash: # if different is present in hash
                return [hash[find],i]
            hash[n]=i
        return