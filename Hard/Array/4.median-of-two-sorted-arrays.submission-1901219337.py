class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array for O(log(min(m, n))) complexity
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            partitionX = (low + high) // 2
            # partitionY handles the remaining elements needed for the left half
            partitionY = (m + n + 1) // 2 - partitionX
            
            # Handle edge cases with -infinity and +infinity
            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == m else nums1[partitionX]
            
            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == n else nums2[partitionY]
            
            # Check if we have found the correct partition
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                # We have partitioned correctly
                
                # If total length is odd, median is the max of the left side
                if (m + n) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                # If total length is even, median is average of boundaries
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0
            
            # If we are too far right in nums1, move left
            elif maxLeftX > minRightY:
                high = partitionX - 1
            # If we are too far left in nums1, move right
            else:
                low = partitionX + 1
                
        raise ValueError("Input arrays are not sorted or invalid.")