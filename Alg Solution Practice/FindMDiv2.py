def findMajority(str, start, end):
    # Find the majority element in an array
    # a majority element is defined if it occurs more than m/2 times in an array
    # where m is the size of the list
    if start == end:    # The majority element in a list of size 1, is that element in the list CONQUER
        return str[start]
    else:
        mid = (start + end) // 2
        # Split the list into two equal halves and find their majority DIVIDE
        l = findMajority(str, start, mid)
        r = findMajority(str, mid+1, end)
        if l == r:  # if the left majority is the same as the right majority, then it is also the combined majority MERGE
            return l
        else:
            # otherwise check if either the leftMaj, or the rightMaj are the combined majority 
            if str.count(l) > (end-start+1)/2:  
                return l
            elif str.count(r) > (end-start+1)/2:
                return r
            else:
                # if neither are, there exists no majority
                return None  
    pass