# Problem: Find the longest substring length without any repeating characters. 
# ex: Input: s = "abcabcbb"
#     Output: 3
#     Explanation: The answer is "abc", with length 3.

# concept: The sliding window
#           have two pointers named l and r. they are both initialised to the start of the array. 
#           the right traverses the array and the left pointer only moves if there is a repitition 
#           also init a dictionary where the char in the key and the value is the index


def longest_sub(ar):
    seen = {}
    max_len = 0
    l = 0
    
    for i in range(len(ar)):
        r = i
        if ar[i] in seen:
            l = max(l, seen[ar[i]] +1)
            seen[ar[i]] = i
        else:
            seen[ar[i]] = i
        max_len= max( max_len, r-l +1)
        
    return max_len


print(longest_sub("abcabcbb"))
        
