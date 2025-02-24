# Given an array of integers nums, return the length of the 
# longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater 
# than the previous element. The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

def main():
    # Input, can be changed
    nums=[9,1,4,7,3,-1,0,5,8,-1,6]
    
    # Made nums a set to get rid of duplicates and then sorted the list
    numSet = set(nums)
    nums = list(numSet)
    nums.sort()

    # Initialize i and j for our sliding window
    i = 0
    j = 1
    # Increment number for sequence
    increment = 1
    # Conditional statement to check whether the list is empty or not
    if len(numSet) == 0:
        ans = 0
    else:
        ans = 1
    # Possible answer keeps track of the current biggest sequence
    posAns = 1
    # While loop that iterates through numSet until j reaches the last number
    while j < len(numSet):
        # Conditional statement to check for a sequence
        if nums[i]+increment == nums[j]:
            # If a sequence does exist, then possible answer, j and increment increase by one
            posAns +=1
            j+=1
            increment +=1
        else:
            # If the sequence does not exist or ended then our sliding window moves over and 
            # we reset our values
            i = j
            j = i+1
            increment = 1
            posAns = 1
            
        # Conditional statement to check if possible answer is greater then our current answer
        if posAns > ans:
            # If possible answer is greater then our answer becomes possible answer
            ans = posAns
    print(ans)
            
    
    
main()