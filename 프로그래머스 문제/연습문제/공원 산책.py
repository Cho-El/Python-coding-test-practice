def solution(park, routes):
    lenX = len(park)
    lenY = len(park[0])
    for x in range(lenX):
        for y in range(lenY):
            if park[x][y] == "S":
                return move(x,y,lenX,lenY,routes,park)

def move(x,y,lenX, lenY, routes, park):
    directDict = {
        "N":[-1,0],
        "S":[1,0],
        "W":[0,-1],
        "E":[0,1]
	}
    for r in routes:
        direction, dist = r.split()
        dist = int(dist)
        movingX, monvingY = x, y
        dx = directDict[direction][0]
        dy = directDict[direction][1]
        while 0 <= movingX + dx< lenX and 0 <= monvingY + dy < lenY \
            and park[movingX + dx][monvingY + dy] != 'X' and dist != 0:
            movingX += dx
            monvingY += dy
            dist -= 1
        
        if dist != 0:
            movingX, monvingY = x, y
        else:
            x,y = movingX, monvingY
        
            
    return [movingX,monvingY]
        
    
    
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))
