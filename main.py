import sys
import io
import os 
import pip
from bfs import bfs
from dfs import dfs
from dls import dls
from ufs import ufs
from greedySearch import greedySearch
from aStarSearch import aStarSearch


try: import easygui
except ImportError:pip.main(["install", "easygui"])

#Author: Himanjal Sharma 
#Run this file to initialize the project 



class graphNodes:
    node1 = ''
    node2 = ''
    cost = 0.0


graph = {}

weightGraph = {}
START = 'S'
GOAL = 'G'


list_of_nodes = []

list_of_heuristic = {}


def addHeuristic(line):

    node = line[0]
    distance = float(line[2:])
    list_of_heuristic[node] = distance

def addNode(line):
    node = graphNodes()
    node.node1 = line[0]
    node.node2 = line[2]
    node.cost = float(line[4:])
    list_of_nodes.append(node)


def createGraph():
    visited = []
    for node in list_of_nodes:
        base = node.node1

        if(base in visited):
            if(node.node2 not in graph[base]):
                graph[base].append(node.node2)
        else:
            visited.append(base)
            graph[base] = []
            graph[base].append(node.node2)
        
        base = node.node2

        if(base in visited):
            if(node.node2 not in graph[base]):
                graph[base].append(node.node1)
        else:
            visited.append(base)
            graph[base] = []
            graph[base].append(node.node1)


def createWeightedGraph():
    visited = []
    for node in list_of_nodes:
        base = node.node1

        if(base in visited):
            if(node.node2 not in weightGraph[base]):
                weightGraph[base].append((node.node2, node.cost))
        else:
            visited.append(base)
            weightGraph[base] = []
            weightGraph[base].append((node.node2, node.cost))
        
        base = node.node2

        if(base in visited):
            if(node.node2 not in weightGraph[base]):
                weightGraph[base].append((node.node1, node.cost))
        else:
            visited.append(base)
            weightGraph[base] = []
            weightGraph[base].append((node.node1, node.cost))     


def readFile():

    graph = easygui.fileopenbox(filetypes = "*.txt", multiple= False)
    #graph = "graph2.txt"
    flag = False
    file = open(graph, "r")
    for line in file:
        line = line[:-1]
        if(line.find("#") > -1):
            flag = True
            continue

        if(flag):
            addHeuristic(line)
        else:
            addNode(line)


def searchSelect(ch):
    if(ch == 1):
        dfs(graph,START,GOAL)
        return
    if(ch == 2):
        bfs(graph, START, GOAL)
        return
    if(ch == 3):
        depth = int(raw_input("Enter Depth :"))
        dls(graph, START, GOAL, depth)
        return
    if(ch == 4):
        ufs(weightGraph, START, GOAL)
        return
    if(ch == 5):
        greedySearch(graph, list_of_heuristic, START, GOAL)
        return
    if(ch == 6):
        aStarSearch(weightGraph, list_of_heuristic, START, GOAL)
        return

def printMenu():
    menu = "\nEnter the Number of the Search\n"
    menu = menu + "\t1. Depth 1st search\n"
    menu = menu + "\t2. Breadth 1st search\n"
    menu = menu + "\t3. Depth Limited Search\n"
    menu = menu + "\t4. Uniform Search\n"
    menu = menu + "\t5. Greedy Search\n"
    menu = menu + "\t6. A* Search\n"
    print menu

    choice = 0
    while(choice not in range(1,6)):
        choice = int(raw_input("Choose a Valid Number:"))

    return choice




readFile()

createGraph()
createWeightedGraph()


answer = "y"

while (answer.upper() == "Y"):
    choice = printMenu()
    searchSelect(choice)
    answer = raw_input("\nContinue Search with a different method?(Yes = Y, No = N)")


os.system("find . -name \"*.pyc\" -exec rm -rf {} \;")

