import io
import sys 
from collections import deque
from ufs import sortQueue

def aStarSearch(graph,distances,start,goal):

	explored = []

	queue = deque()
	startPathCost = 0 + distances[start]
	queue.append((startPathCost,[start]))

	costGraph = {}

	costGraph['S'] = (startPathCost, 0)

	while queue:

		print queue[0][1][0] , "\t\t", list(queue)

		node = queue.popleft()

		base = node[1][0]

		if(base == goal):
			print"Reached Goal"
			return True

		baseCost = node[0]

		if(base in explored):
			if(costGraph[base]< baseCost):
				continue
		else:
			explored.append(base)

		


		neighbours = graph[base]

		for neighbour in neighbours:
			cost = neighbour[1] + distances[neighbour[0]] + costGraph[base][1]

			childNode = [neighbour[0]] + node[1]
			
			if(neighbour[0] in costGraph):
				if(costGraph[neighbour[0]][0] < cost):
					continue

			costGraph[neighbour[0]] = (cost, costGraph[base][1] + neighbour[1])
			queue.append((cost,childNode))

		queue = sortQueue(queue)
		


def compareCost(node, queue):
	base = node[1][0]

	if base == 'S':
		return False, queue
	baseCost = node[0]
	flag = True

	newQ = deque()
	tempQ = list(queue)

	for item in tempQ:
		#print base , "base " , item[1][0], "queue end"
		if(item[1][0] == base):
			flag = False
			#print base
			if(baseCost < item[0]):
				#print"baseCost", baseCost, " itemCost", item[0]
				flag = True
				continue
		newQ.append(item)

	return flag, newQ
