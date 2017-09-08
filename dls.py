import io 
import sys 
from collections import deque


def dls(graph, start, goal, depth):


	print"Depth Limited Search"
	print"Expansion\tQueue"
	explored =[]
	queue = deque()
	for i in range(0,depth+1):
		print"Depth ", i
		queue.clear()
		queue.append([start])
		found = depthLimitedSearch(queue, goal, graph, i, explored)
		if(found):
			print"Goal Reached"
			return found
		
	print "Goal Not Reached"
	return False


def depthLimitedSearch(queue, goal, graph, depth, explored):

	if(len(queue) < 1):
		return False

	
	

	node = queue.popleft()
	base = node[0]

	if((base,depth) in explored):
		return False

	explored.append((base,depth))


	print base , "\t\t", [node] + list(queue)

	if(base == goal):
		return True

	if(depth == 0):
		return False
	

	neighbors = sorted(graph[base])

	for neighbor in reversed(neighbors):
		queue.appendleft([neighbor] + node)

	for neighbor in neighbors:
		#print"queue" , queue
		flag = depthLimitedSearch(queue, goal, graph, depth -1, explored)
		if(flag):
			return True
		
	return False