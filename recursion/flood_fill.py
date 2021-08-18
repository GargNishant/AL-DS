# https://www.youtube.com/watch?v=R1URUB6_y2k&list=PL-Jc9J83PIiFxaBahjslhBD1LiJAV7nKs&index=48

def flood_fill(visited:list,curr:tuple=(0,0),ans='',dest:tuple=(0,0)):
    if curr[0] == dest[0] and curr[1] == dest[1]:
        print(ans)
        return
    if curr[0] >= len(matrix) or curr[0] < 0\
            or curr[1] >= len(matrix[0]) or curr[1] < 0\
            or matrix[curr[0]][curr[1]] == 1\
            or visited[curr[0]][curr[1]] == True:
        return
    visited[curr[0]][curr[1]] = True
    # Up
    flood_fill(visited=visited, curr=(curr[0] - 1, curr[1]), ans=ans + "t", dest=dest)
    # Left
    flood_fill(visited=visited, curr=(curr[0], curr[1] - 1), ans=ans + "l", dest=dest)
    # Down
    flood_fill(visited=visited, curr=(curr[0] + 1, curr[1]), ans=ans + "d", dest=dest)
    # Right
    flood_fill(visited=visited, curr=(curr[0], curr[1] + 1), ans=ans + "r", dest=dest)
    visited[curr[0]][curr[1]] = False

if __name__ == "__main__":
    vsf = [[False,False,False],[False,False,False],[False,False,False]]
    matrix = [[0,1,0],[0,0,1],[0,0,0]]
    flood_fill(vsf,(0,0),'',(2,2))


