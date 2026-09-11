# problem: You are given two integer arrays nums1 and nums2, 
#           sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

#           Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#           The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
#           To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
#            and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# concept: The main issue with have the final result in the first array is inserting new values, so we should start by placing the largest number to the back of the array
#           instead of the smallest number.

def merged_arrays(ar1, len1, ar2, len2):
    pointer1 = len1 - 1          # last real element in ar1
    pointer2 = len2 - 1          # last real element in ar2
    pointer3 = len1 + len2 - 1   # last slot in the merged array

    while pointer2 >= 0:
        if pointer1 >= 0 and ar1[pointer1] > ar2[pointer2]:
            value = ar1[pointer1]
            pointer1 -= 1
        else:
            value = ar2[pointer2]
            pointer2 -= 1

        ar1[pointer3] = value
        pointer3 -= 1

    return ar1


print(merged_arrays([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))




