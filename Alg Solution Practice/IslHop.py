def island_hopping(c,n):    # Solving the island hopping (1 or 2 steps) problem using Dynamic Programming
    arr = []
    path = []
    arr.append(0)
    path.append("0")
    arr.append(c[0])
    path.append("0-1")
    for i in range(2,n):
        option1 = c[i-1] + arr[i-1]
        option2 = c[i-2] + arr[i-2]
        if option1 < option2:
            arr.append(option1)
            path.append(path[i-1] + "-" + i)
        else:
            arr.append(option2)
            path.append(path[i-2] + "-" + i) 
    return(arr[n], path[n])
