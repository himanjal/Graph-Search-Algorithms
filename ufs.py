import io 
import sys 
from collections import deque

def ufs(graph, start, goal):

	explored = []
	queue = deque()
	queue.append((0,['S']))

	print"Uniform Search"
	print"Expansion\tQueue"

	while queue:


		print queue[0][1][0] , "\t\t" , list(queue)
		node = queue.popleft()
		#print node
		base = node[1][0]
		#print base
		
		if(base == goal):
			print "Goal Reached"
			return True

		if base not in explored:
			explored.append(base)
			neigbours = graph[base]

			for neigbour in reversed(neigbours):
				if(neigbour[0] in explored):
					continue
				cost  = node[0] + neigbour[1]
				newnode = [neigbour[0]] + node[1]
				queue.appendleft((cost, newnode))
			
			queue = sortQueue(queue)


	print"Goal Not Reached"
	return False

def sortQueue(queue):

	tempQ = list(queue)

	newQ = deque()
	while len(tempQ) > 0:
		smallCost = tempQ[0][0]
		smallNode = tempQ[0][1]
	 	for item in tempQ:
	 		if(item[0] < smallCost):
		 		smallCost = item[0]
		 		smallNode = item[1]

		newQ.append((smallCost,smallNode))
		tempQ.remove((smallCost,smallNode))

		
	return newQ