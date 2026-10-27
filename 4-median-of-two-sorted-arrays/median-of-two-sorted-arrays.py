class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Step 1: Merge both arrays
          merged = nums1 + nums2


    # Step 2: Sort the merged array
          merged.sort()

    # Step 3: Find the length
          n = len(merged)

    # Step 4: Find the middle index
          mid = n // 2

    # Step 5: Calculate the median
          if n % 2 == 1:
            return float(merged[mid])
          else:
             left = merged[mid - 1]
             right = merged[mid]
             return (left + right) / 2.0

       

