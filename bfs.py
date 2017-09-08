import io
from collections import deque
import sys
import os


def bfs(graph, start, goal):
    explored = []
    queue = deque([start])

    print"Breadth First Search"
    print"Expansion\tQueue"
    while queue:

        print queue[0][0] , "\t\t" , list(queue)
        node = queue.popleft()
        base = node[0]

        

        if base not in explored:
            explored.append(base)

            if(base == goal):
                print "Goal Reached"
                return explored

            neighbours = sorted(graph[base])
            #print"base", base , "\t\tNeighbours" , neighbours
            for neighbour in neighbours:
                if neighbour in explored:
                    continue
                temp = []
                temp.append(neighbour)
                for ch in node:
                    temp.append(ch)
                queue.append(temp)
                

    print"Goal Not Reached"
    return explored


