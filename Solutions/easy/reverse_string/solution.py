#Problem: Write a function that reverses a string. The input string is given as an array of characters s.
#         You must do this by modifying the input array in-place with O(1) extra memory.

#Example 1:

#   Input: s = ["h","e","l","l","o"]
#   Output: ["o","l","l","e","h"]

#Example 2:

#   Input: s = ["H","a","n","n","a","h"]
#   Output: ["h","a","n","n","a","H"]

#concept: have two pointers, one at the end and begining of the string.
#         then swap characters and iterate twords the center of the array
#         the while condition will handle unever lengths

def ReverseString(arr):
    length = len(arr)
    leftp =0
    rightp= length-1

    if length <= 1:
        return arr
    

    while leftp < rightp:
        char1 = arr[leftp]
        char2 = arr[rightp]
        arr[leftp] = char2
        arr[rightp] = char1
        leftp = leftp +1
        rightp = rightp -1
    return arr

print(ReverseString(["h","e","l","l","o"]))


