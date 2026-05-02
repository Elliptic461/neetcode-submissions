class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        total = len(nums1) + len(nums2) 
        # Half tells us the total number for the left partition
        half = total // 2

        # Want A to contain the smaller array
        if len(B) < len(A):
            A, B = B, A
        
        #Run binary search
        left, right = 0, len(A) - 1
        while True:
            i = (left + right) // 2 # Pointer for A
            j = half - i - 2 # Pointer for B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                #odd
                if total % 2:
                    # Runtime: O(log(m + n))
                    return min(Aright, Bright)
                #even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # Too many elements from A, reduce A
            elif Aleft > Bright:
                right = i - 1
            # Bleft <= Aright is not true, increase A
            else:
                left = i + 1










        