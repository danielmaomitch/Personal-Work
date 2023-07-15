import time, random
def BFSubArray(arr):
    size = 1
    max = -100000
    subArr = []
    cur = 0
    while (size < len(arr)):
        index = 0
        while ((index+size-1) < len(arr)):
            cur = sum(arr[index:index+size])
            if cur > max:
                max = cur
                subArr = arr[index:index+size]
            index += 1
        size += 1
    return subArr

def crossingSubArray(arr):
    # find the max sub array that crosses the midpoint, linear time complexity 
    mid = len(arr) // 2
    leftMax, rightMax = [], []
    curMax = -100000
    index = mid
    while index >= 0:   # go to the left
        if sum(arr[index:mid]) > curMax:
            leftMax = arr[index:mid]
            curMax = sum(arr[index:mid])
        index -= 1
    curMax = -100000
    while index <= len(arr):    # go to the right
        if sum(arr[mid+1:index]) > curMax:
            rightMax = arr[mid+1:index]
            curMax = sum(arr[mid+1:index])
        index += 1
    return leftMax + rightMax


def smartSubArray(arr):
    if (len(arr) <= 5): # Base case: brute force it at size 5
        return BFSubArray(arr)
    mid = len(arr) // 2
    # divide the array into two equal halves and find their maxSubArray
    leftMax = smartSubArray(arr[:mid])
    rightMax = smartSubArray(arr[mid+1:])
    # combine by finding if the max array is crossing the middle point
    midMax = crossingSubArray(arr)
    
    # return the max(left, right, middlecrossing)
    leftSum = sum(leftMax)
    rightSum = sum(rightMax)
    midSum = sum(rightMax)

    if (leftSum > rightSum) and (leftSum > midSum):
        return leftMax
    elif (rightSum > leftSum) and (rightSum > midSum):
        return rightMax
    else:
        return midMax

def main():
    arr = [4,6,-10,-2,500,-800,-10, 3, 104, 206, -5, 1000, 60]
    arr = []
    for i in range(1000):
        arr.append(random.randint(-100, 100))
    start = time.time()
    results = BFSubArray(arr)
    end = time.time()
    BFTime = end - start
    print(f"Brute force took: {end - start} ns")
    print(results)
    start = time.time()
    results = smartSubArray(arr)
    end = time.time()
    print(f"DnC algorithm took: {end - start} ns")
    print(results)
    ratio = (BFTime / (end - start)) * 100
    print(f"DnC is {ratio}% faster")
    print("done")
    return 0

    #check how long each one takes
main()
    