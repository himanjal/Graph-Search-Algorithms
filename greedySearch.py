import sys 
import io 
from collections import deque
from ufs import sortQueue


def greedySearch(graph, distances, start, goal):
	explored = []
	queue = deque()

	queue.append((distances[start], [start]))


	print "Greedy Search"
	print "Expansion\tQueue"
	while queue:

		print queue[0][1][0] , "\t\t" , list(queue)

		node = queue.popleft()

		base = node[1][0]

		if(base == goal):
			print"Goal Reached"
			return True

		if base not in explored:

			explored.append(base)

			neighbours = graph[base]

			for neighbour in neighbours:
				cost = distances[neighbour]
				childNode = [neighbour] + node[1]
				queue.append((cost, childNode))


		queue = sortQueue(queue)


	print"Goal Not Reached"
	return False
