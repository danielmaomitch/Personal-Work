def FindPairSum(arr, k):
    # Find if there is a pair x and y in a sorted list S that sum to k
    # This solution takes advantages of the fact the list is sorted
    n = len(arr)
    l = 0
    r = n-1
    # start at each opposing end and check their sum
    while l < n and r >= 0:
        pairSum = arr[l] + arr[r]
        
        if pairSum == k:    # if we found the sum return
            return l,r
        elif pairSum < k:   # if the sum < k then move l up
            # if the largest value in S plus another value x in S is still too small, make x larger
            l += 1
        else:   # if sum > k then move r down
            # if the smallest value plus some element y is too large, make y smaller
            r -= 1
    return None

def TwoSetSum(arr1, arr2, k):
    # Find if given two sets X and Y, tere exist and xEX and yEY where x + y = k
    # This solution is more or less identical to the PairSum solution
    n = len(arr1)
    m = len(arr2)
    l = 0
    r = m - 1
    while l < n and r >= 0:
        pairSum = arr1[l] + arr2[r]

        if pairSum == k:
            return l,r
        elif pairSum < k:
            l += 1
        else:
            r -= 1
    return None

if __name__ == "__main__":
    testArr = [1,2,3,4,5,6,7,8,9]
    testArr2 = [10,11,12,13,14,15,16,17,18,19,20]
    testK = 15
    print(FindPairSum(testArr, testK))
    print(TwoSetSum(testArr, testArr2, testK))
