# Given an integer array nums, return an array output where output[i] is the product of all 
# the elements of nums except nums[i].
# Each product is guaranteed to fit in a 32-bit integer.
# Follow-up: Could you solve it in O(n) time without using the division operation?

def main():
    # Input, can be changed
    nums = [1,2,4,6]
    
    # set a prefix and postfix with their initial values
    # pre will have an initial value of the first index
    pre = [nums[0]]
    # post will have an initial value of the last index
    post = [nums[len(nums)-1]]
    # set the multiples of each before going through the loop
    preMultiple = pre[0]
    postMultiple = post[0]
    
    # list for answer
    ans = []
    
    # for loop that iterates through nums and calculates the multiples of prefix and postfix
    for i in range(len(nums)-1):
        preMultiple *= nums[i+1]
        postMultiple *= nums[len(nums)-2-i]
        # append each multiple
        pre.append(preMultiple)
        post.append(postMultiple)
    
    # reverse post since it is appended backwards
    # for example the last number in nums is the first number in post but it should be the last
    post.reverse()
    
    # for each number in pre, the number on the left of it is multiplied by the post 
    # number on the right to get the answer
    
    # since the number on the left of pre doesn't exist, it becomes a one and we are left with post[1] 
    ans.append(post[1])
    # for loop that iterates through length of pre starting with one since we already got the answer for zero
    for i in range(1,len(pre)-1):
        # for each number in pre starting with index one we can append the 
        # pre number before and the post number after i
        ans.append(pre[i-1]*post[i+1])
    # since the number on the right of post doesn't exist, it becomes a one and we are 
    # left with the second to last value in pre 
    ans.append(pre[len(pre)-2])
    
    # After we append everything, we have the answer
    print(ans)
        
main()