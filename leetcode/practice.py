# NEARBY ALMOST DUPLICATE
# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
#         if k < 1 or t < 0:
#             return False
#         dic = OrderedDict()
#         for n in nums:
#             key = n if not t else n // t
#             for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
#                 if m is not None and abs(n - m) <= t:
#                     return True
#             if len(dic) == k:
#                 dic.popitem(False)
#             dic[key] = n
#         return False

# 53 MAXIMUM SUBARRAY
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         currSub, maxSub = nums[0], nums[0]
#         for number in nums[1:]:
#             currSub = max(number, currSub + number)
#             maxSub = max(currSub, maxSub)
#         return maxSub

# 1 Two Sum
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         hash_table = {}
#         for i in range(len(nums)):
#             if nums[i] in hash_table:
#                 return [hash_table[nums[i]], i]
#             else:
#                 hash_table[target - nums[i]] = i

# 88 MERGE SORTED ARRAY
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        pos = m+n
        while m > 0 and n > 0:
            pos -= 1
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[pos] = nums1[m - 1]
                m -= 1
            else:
                nums1[pos] = nums2[n - 1]
                n -= 1
        while n > 0:
            pos -= 1
            nums1[pos] = nums2[n-1]
            n -= 1
