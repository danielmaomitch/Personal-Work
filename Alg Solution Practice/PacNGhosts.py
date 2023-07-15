def pacman_shortest_path(ghost):
    P = []
    P[0][0] = 1*(1 - ghost[0][0])
    n = ghost.length()
    for i in range(1, n):
        P[0][i] = 1*(1 - ghost[0,i])
    for i in range(1, n):
        P[i][0] = 1*(1 - ghost[i][0])
    for i in range(1, n):
        for j in range(1, n):
            P[i][j] = (P[i-1][j])*(1 - ghost[i-1][j]) + (P[i][j-1])*(1 - ghost[i][j-1])
    return P[n-1][n-1]
    pass