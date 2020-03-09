print("DEPTH FIRST SEARCH ALGORITHM")
print("The graph is implemented using dictionaries. The structure of the dictionary is as follows: {Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...},Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...} and so on\n\n")

graph = {'A':['B','S'],
         'B':['A'],
         'S':['A','C','G'],
         'C':['D','E','F','S'],
         'G':['F','H','S'],
         'E':['C','H'],
         'F':['C','G'],
         'D':['C'],
         'H':['E','G']}
startNode = 'A'
goalNode = 'H'
print("Start Node: ",startNode)
print("Goal Node: ",goalNode)
open = [startNode]
closed = []
paths = [startNode]
path_found = False
came_from = {}
print("We define the following variables: \nopen: Stack containing nodes left to explore. Initialized with start node. \nclosed: List of explored nodes. \ncame_from: Dictionary containing parent node of every node")
print("\nInitially, closed = ",closed,"open = ",open,"came_from = ",came_from)
print("\n\n #################### Algorithm begins here. Iterations end when open is empty #####################")
iter = 1
while len(open)!=0:
    print("                             \nITERATION ", iter)
    currentNode = open[len(open)-1]
    print(" Current node is the top of open stack:",currentNode)
    # print(currentNode)
    explored = True
    print("Iterate over every neighbour of current Node ") #check if it is goal node, set path_found to True and came_from of this neighbour to currentNode. \nElse, if the neighbour is neither already explored nor in the open stack,"
          #"add this neighbour to open stack and set came_from for this neighbour to currentNode. Now stopmove on to next ")
    for i in graph[currentNode]:
        print("Neighbour:",i)
        print("is ",i," the goal node?")
        if i == goalNode:
            print("yes. Then set path_found to true and came_from for ",i," to ",currentNode," and stop algorithm")
            path_found = True
            came_from[i] = currentNode
            break
        print("No. Then is the neighbour is neither already explored nor in the open stack?")
        if i not in closed and i not in open:
            print("Yes. Then add ",i," to open stack and set came_from for ",i," to ",currentNode," and stop analyzing neighbours")
            open.append(i)
            explored = False
            came_from[i] = currentNode
            break
        print("No. Next neighbour.")

    print("Have we found a path?")
    if path_found == True:
        print("Yes. The path is:")
        i = came_from[goalNode]
        path = [goalNode]
        while i != startNode:
            path.append(i)
            i = came_from[i]
        path.append(startNode)
        path.reverse()
        print(path)
        break
    print("No.")
    print("Have we explored all neighbours of ",currentNode,"?")
    if explored == True:
        print("Yes. Then remove ",currentNode," from open and put it in closed")
        open.pop()
        closed.append(currentNode)
    print("No.")
    print("After iteration number", iter, "\nopen = ", open, "\nclosed = ", closed, "\ncame_from = ",
          came_from)
    iter = iter+1

# print(final_series)
