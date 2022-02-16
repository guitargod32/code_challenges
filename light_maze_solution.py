#oreintation denotes direction light is headed 1: right, 2: left, 3:down, 4:up
#loc[0] is x
#loc[1] is y
#path = []
#helper functions for moving in a given direction
def moveRight(maze,loc,path):
    if loc[1]+1 < len(maze[0]):
        isAngled(path,maze,(loc[0],loc[1]+1),maze[loc[0]][loc[1]+1],1)
    else:
        print("check")
        return(path)
        

def moveLeft(maze,loc,path):
    if loc[1]-1 >= 0:
        isAngled(path,maze,(loc[0],loc[1]-1),maze[loc[0]][loc[1]-1],2)
    else:
        print("here")
        return(path)
        

def moveDown(maze,loc,path):
    if loc[0]+1 < len(maze):
        isAngled(path, maze, (loc[0]+1, loc[1]),maze[loc[0]+1][loc[1]],3)
    else:
        print("check")
        return(path)
        
def moveUp(maze,loc,path):
    if loc[0]-1 >= 0:
        isAngled(path,maze,(loc[0]-1,loc[1]),maze[loc[0]-1][loc[1]],4)
    else:
        print("check")
        return(path)
        
        
#add location to the route, then check if it contains a mirror and turn accordingly
def isAngled(path, maze,loc,nextNum, orientation):
    path.append(loc)
    #moving to the right
    if  (nextNum) < 0 and orientation == 1:
        moveDown(maze,(loc), path)
    elif (nextNum) > 0 and orientation ==1:
        moveUp(maze,loc,path)
    elif orientation == 1:
        moveRight(maze, (loc), path)
    else:
        return(path)
    #moving to the left  
    if (nextNum) < 0 and orientation == 2:
        moveUp(maze,loc,path)
    elif (nextNum) > 0 and orientation ==2:
        moveDown(maze,loc,path)
    elif orientation ==2:
        moveLeft(maze,loc,path)
    else:
        return(path)
    #moving downawrds
    if (nextNum) > 0 and orientation == 3:
        moveLeft(maze,loc,path)
    elif (nextNum) < 0 and orientation ==3:
        moveRight(maze, loc, path)   
    elif orientation ==3:
        moveDown(maze,loc,path)
    else:
        return(path)
    #moving upwards
    if nextNum > 0 and orientation ==4:
        moveRight(maze,loc,path)
    elif nextNum < 0 and orientation ==4:
        moveLeft(maze,loc, path)
    elif orientation == 4:
        moveUp(maze,loc,path)
    else:
        return(path)
       
        
#execute the program. maze always starts at (0,0) and heading to the right.
def maze_solver(maze):
    path = []
    newpath = isAngled(path, maze, (0,0), maze[0][0], 1)
    return newpath
    
    