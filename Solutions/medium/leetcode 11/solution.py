#Container With Most Water — nice one, it's a classic two-pointer problem.

#The setup: You get an array height, where height[i] is the height of a vertical 
#           line at position i. Pick two lines; together with the x-axis they 
#           form a container. Maximize the water it can hold.

#concept: start on both ends of the array, since thats the max width.
#         then clac the area
#         area = min(height[left], height[right]) * right-left
#         then move the pointer with the shorter height
#         after iterating through the array, return max


def Mostwater(arr):
    left_index = 0
    right_index = len(arr) -1
    m = 0
    while left_index < right_index:
        lowest_height = min(arr[left_index], arr[right_index])
        area = lowest_height * (right_index- left_index +1)
        print(area, lowest_height)
        m = max(m, area)

        if arr[left_index] > arr[right_index]:
            right_index = right_index -1
        else:
            left_index = left_index +1
    return m

print(Mostwater([1,1,1,1]))


