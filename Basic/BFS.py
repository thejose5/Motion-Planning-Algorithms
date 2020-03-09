print("DEPTH FIRST SEARCH ALGORITHM")
print("The graph is implemented using dictionaries. The structure of the dictionary is as follows: {Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...},Node1:{NeighbourNode1:[<distance b/w nodes>,<heuristic>],...} and so on\n\n")

graph = {'A':['S','B'],
         'B':['A'],
         'S':['G','C','A'],
         'C':['E','F','D','S'],
         'G':['S','F','H'],
         'E':['H','C'],
         'F':['C','G'],
         'D':['C'],
         'H':['G','E']}
startNode = 'A'
goalNode = 'H'
print("Start Node: ",startNode)
print("Goal Node: ",goalNode)
#currentNode = startNode
open = [startNode]
closed = []
paths = [startNode];
flag = False
print("We define the following variables: \nopen: Queue containing nodes left to explore. Initialized with start node. \nclosed: List of explored nodes. \npaths: Queue of all possible paths")
print("\nInitially, closed = ",closed,"open = ",open," paths = ",paths)
print("\n\n #################### Algorithm begins here. Iterations end when open is empty #####################")
iter = 1
while len(open)!=0:
    print("                             \nITERATION ", iter)
    currentNode = open.pop(0)
    print(" Current node is the top of open queue:", currentNode)
    adm_nbrs = [];
    print("Iterate over every neighbour of current Node ")
    for i in range(len(graph[currentNode])):
        print("Neighbour:", graph[currentNode][i])
        print("is ", graph[currentNode][i], " the goal node?")
        if graph[currentNode][i] == goalNode:
            print("Yes")
            flag = True
            break
        print("No. Then is the neighbour is neither already explored nor in the open stack?")
        if graph[currentNode][i] not in closed and graph[currentNode][i] not in open:
          print("Yes. Then add ",graph[currentNode][i]," to open and also set it as an admissible neighbour.")
          open.append(graph[currentNode][i])
          # print(open)
          adm_nbrs.append(graph[currentNode][i])
    if flag==True:
        print("Then set final series as the top of the paths queue + the goal node")
        final_series = paths.pop(0)+goalNode
        break;
    print("After iterating through all neighbours of ",currentNode," add it to closed")
    closed.append(currentNode)

    # print(adm_nbrs)
    print("Add new items to back of path queue. Each of these paths will be the path till current node + 1 of the admissible neighbours")
    prev_series = paths.pop(0)
    for i in adm_nbrs:
        # prev_series = prev_series+i
        paths.append(prev_series+i)
    print("After iteration number", iter, "\nopen = ", open, "\nclosed = ", closed, "\npaths = ",
          paths)
    iter = iter+1
    # print(prev_series)
print("The final path is")
print(final_series)
    #print(currentNode)
