def FindSingleLetter(arr):
    mid = len(arr) // 2
    if (len(arr) == 0):
        return None
    elif (arr[mid] == arr[mid+1]) & (arr[mid] == arr[mid-1]):
        return None
    elif (arr[mid] != arr[mid+1]) & (arr[mid] != arr[mid-1]):
        return mid
    elif (mid % 2 == 1):
        if (arr[mid] == arr[mid-1]):
            return FindSingleLetter(arr[mid:])
        else:
            return FindSingleLetter(arr[:mid])
    else:
        if (arr[mid] == arr[mid+1]):
            return FindSingleLetter(arr[mid:])
        else:
            return FindSingleLetter(arr[:mid])


def FindSingleLetter2(str, start, end):
    # In a string with double repeating letters, find the letter that does not repeat
    # strings will only look like "aabbcczddee" etc
    # assume a string is valid
    # invalid strings are triple repeating, or multiple single letters
    print(start, end)
    if start > end: # if we have search the whole array, there is no single letter
        return None
    elif start == end:  # utilize the math of a double repeating list to know that the array will only have one element if there is a single letter
        return start
    else:
        mid = (start + end) // 2

        # utilize the geometry of a double repeating array to know that if the repeat start is even
        # then it is on the left side of the single element
        # and if it is odd, it is on the right side of the single letter
        # since the single letter will offset the pattern
        if mid % 2 == 0:
            # for the case of even index
            if str[mid] == str[mid+1]:  # if the repeats starts on the current index, skip past and search the right half
                return FindSingleLetter2(str, mid+2, end)
            else:
                return FindSingleLetter2(str, start, mid)   # if the index is even but isnt the start of the repeat, search the left half
        else:
            if str[mid] == str[mid-1]:  # odd index case
                return FindSingleLetter2(str, mid+1, end)   # if odd index and ends the repeat, serach the right half
            else:
                return FindSingleLetter2(str, start, mid-1)     # if odd and index doesnt end the repeat, search the left half


def main():
    someLetts = "aabbccddeeff"
    print(FindSingleLetter2(someLetts, 0, len(someLetts)-1))
    return 0

main()