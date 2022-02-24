# 704 BINARY SEARCH

# def search(self, nums: List[int], target: int) -> int:
#     l = 0
#     r = len(nums)

#     while (l < r):
#         mid = l + (r - l)//2
#         if nums[mid] == target:
#             return mid
#         if nums[mid] > target:
#             r = mid
#         if nums[mid] < target:
#             l = mid + 1
#     return -1


# 278 FIRST BAD VERSION
# class Solution:
#     def firstBadVersion(self, n: int) -> int:
#         st = 0
#         end = n

#         while st < end:
#             mid = st + (end - st)//2
#             if isBadVersion(mid) == True:
#                 end = mid
#             else:
#                 st = mid +1
#             return end


# 2 Add two linked lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         cur = dummy

#         carry = 0
#         while l1 or l2 or carry:
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0

#             # new digit
#             val = v1 + v2 + carry
#             carry = val // 10
#             val = val % 10
#             cur.next = ListNode(val)

#             # update pointers
#             cur = cur.next
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None

#         return dummy.next

# 3 LONGEST SUBSTRING WITH NO DUPES
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0
#         for r in range(len(s)):
#             while s[r] in charSet:
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r])
#             res = max(res, r - l + 1)
#         return res


# 4 MEDIAN OF TWO SORTED ARRAYS
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         A, B = nums1, nums2
#         total = len(nums1) + len(nums2)
#         half = total // 2

#         if len(B) < len(A):
#             A, B = B, A

#         l, r = 0, len(A) - 1
#         while True:
#             i = (l + r) // 2  # A Pointer
#             j = half - i - 2  # B Pointer

#             Aleft = A[i] if i >= 0 else float("-infinity")
#             Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
#             Bleft = B[j] if j >= 0 else float("-infinity")
#             Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

#             if Aleft <= Bright and Bleft <= Aright:
#                 # odd
#                 if total % 2:
#                     return min(Aright, Bright)
#                 # even
#                 return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
#             elif Aleft > Bright:
#                 r = i - 1
#             else:
#                 l = i + 1

# 5 LONGEST PALINDROMIC SUBSTRING
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         res = ""
#         resLen = 0

#         for i in range(len(s)):
#             #odd length palindromes
#             l, r = i, i
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if(r - l + 1) > resLen:
#                     res = s[l:r+1]
#                     resLen = r - l + 1
#                 l -= 1
#                 r += 1

#             #even length
#             l, r = i, i + 1
#             while l >= 0 and r < len(s) and s[l] == s[r]:
#                 if (r - l + 1) > resLen:
#                     res = s[l:r+1]
#                     resLen = r - l + 1
#                 l -= 1
#                 r += 1
#         return res

# 6 ZIGZAG CONVERSION
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s

#         res = ""
#         for r in range(numRows):
#             increment = 2 * (numRows - 1)
#             for i in range(r, len(s), increment):
#                 res += s[i]
#                 if (r > 0 and r < numRows - 1 and
#                         i + increment - 2 * r < len(s)):
#                     res += s[i + increment - 2 * r]
#         return res

# 7 REVERSE INTEGER
def reverse(x: int):
    for i in x:
        print(i)


reverse(123)
