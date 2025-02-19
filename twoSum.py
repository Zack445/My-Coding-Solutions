#Q: Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.
def main():
    # sample numbers, can be changed
    nums = [3,4,5,6]
    target = 7

    # Creating our window
    i=0
    j=1
    ans = None
    # if i is on the last number we know it is not possible for nums to meet the target
    while i<len(nums)-1:
        # rearange our addition to find what our second number needs to be to hit the target
        targetNum = target - nums[i]
        # if we find the second number we set ans to the index of those numbers
        if targetNum == nums[j]:
            ans = [i,j]
            break
        else:
            # increase the right side of our window if we don't find target
            j+=1
        if j == len(nums):
            # if j goes past the end we know to move the left side of the window and retry
            i+=1
            j=i+1
    # print our answer
    print(ans)
main()  