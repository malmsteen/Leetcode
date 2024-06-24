from typing import *


def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    out = [0] * l
    # for i, v in enumerate(nums):
    #     idx = (i + k) % l
    #     out[idx] = nums[i]
    idx = k % l
    return nums[idx:]+nums[:idx]


x = list(range(1, 11))
print(x)
print(rotate(x, 2))
