#You are given an integer array heights where heights[i] represents the height of the ith bar.

#You may choose any two bars to form a container. Return the maximum amount of water a container can store.

def main():
    # Input, can be changed
    heights = [1,7,2,5,4,7,3,6]
    
    # Intialize i and j to be at the beginning and end of the list
    i = 0
    j = -1
    
    # Distance is the distance between i and j which to start is the length of height minus 1
    distance = len(heights)-1
    
    # Initialize answer and possible answer to 0
    ans = 0
    posAns = 0
    
    # While loop that goes until i and j converge leaving no distance between them
    while distance > 0:
        # Conditional statement that checks to see which end is smaller
        if heights[i] < heights[j]:
            # If the left end is smaller then we set that as our lowest wall and the lowest idx
            lowestWall = heights[i]
            lowestIdx = i
        else:
            # If the right end is smaller then we set them to our lowest wall and lowest idx instead
            lowestWall = heights[j]
            lowestIdx = j
        # Possible answer is the area between the distance and our lowest wall.
        posAns = distance * lowestWall
        # If our current possible answer is greater then our answer we replace our answer with the new value
        if posAns > ans:
            ans = posAns
        # The distance between i and j gets decreased by 1 and we check to see which side was the lowest
        distance -= 1
        # If the right side was the lowest then the idx would be negative and we can subtract 1
        if lowestIdx < 0:
            j -=1
        # If the left side was the lowest then the idx would be positive and we can add 1
        else:
            i+=1
    # Print answer outside of the loop
    print(ans)
    
    
main()