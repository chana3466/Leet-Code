## Problem: Given an array of integers nums and an integer target, 
#           return the indices of the two numbers that add up to target. 
#           You may assume exactly one solution exists, 
#           and you can't use the same element twice.


# concept: since there's one solution, you can subtract the target from the number you are currently looking at to 
#          see the value you must have to make that number apart of the solution. So you can create a dictionary, the keys being the number
#          and the value being the index where that number in present in the array. 
#
#          So as you traverse in the array you can add nums to the dictionary while also checking if their corelated number is also present.


def twoSums(target, ar):
    dic = {}
    for x in range(len(ar)):
        comp = target - ar[x]
        if comp in dic:
            return (dic[comp], x)
        else:
            dic[ar[x]] = x
    return -1

# Testing

print(twoSums(3,[1,2,4,3]))
print(twoSums(1, [1,2,3,4]))
