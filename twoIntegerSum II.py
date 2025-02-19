# Q: Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], 
# such that they add up to a given target number target and index1 < index2. 
# Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.
# There will always be exactly one valid solution.
# Your solution must use O(1) additional space.
def main():
    # program input, can be changed
    numbers=[-5,-3,0,2,4,3,8]
    target=0
    
    # left and right of sliding window
    l = 0
    r = 1
    found = False
    
    # find is the remainder of target minus the left number in the window
    find = target - numbers[l]
    
    while l < len(numbers)-1:
        # if we find our value then we print the indexes plus 1
        if numbers[r] == find:
            print([l+1,r+1])
            found = True
            break
        r+=1
        # if the right side of our window reaches the end we move our left side of the 
        # window and reset our right side.
        if r == len(numbers):
            l += 1
            r = l + 1
            find = target - numbers[l]
    # Although not needed since the prompt said there would always be a solution I added a check just in case
    # target can not be made
    if not found:
        print("Can not make target number!")
    
main()
