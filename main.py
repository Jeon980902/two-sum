from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
  array_len = len(nums)
  for i in range (0, array_len):
    for j in range (i+1, array_len):
        if (nums[i] + nums[j] == target):
            return [i,j]
  return []
