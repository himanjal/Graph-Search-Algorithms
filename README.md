# Graph-Search-Algorithms

The search strategies included in this project are:

* Depth 1st search
* Breadth 1st search
* Depth-limited search (use depth-limit = 2)
* Iterative deepening search (show all iterations, not just the iteration that succeeds)
* Uniform cost search (= Branch-and-bound)
* Greedy search (= Best 1st search)
* A*

# Input Specifications:

The graph file has two sections.  The first section describes the topology of the graph and the weights (costs, distances) of the paths between nodes.  The second section provides heuristic estimates for the distances from each node to the goal node.

In the first section, each line contains all the information about one connection between two adjacent nodes.  Each of these lines has 3 fields, and each field is separated by whitespace. 

* The first field is the name of a node.  All nodes are named by a single capital letter.  Therefore, the length of the first field is always one byte (one character).
* The second field is also the name of a node, and is also one character long.  In the graph, this node is adjacent to the node named in the first field.
* The third field is the actual length of the connection between the node named in the first field and the node named in the second field.  It is a float value.

In total, the first section will contain as many lines as there are connections in the graph.  You may assume that every graph contains a node named 'S' and a node named 'G'.  You may also assume that the graph is finite (of course).  These are the starting and goal nodes, respectively.  After the first section there will be a line separating the two sections.  This line will contain only 5 pound signs.  i.e. "#####"

The second section contains heuristic information about each node in the graph (except for the goal node).  Only the heuristically informed methods should use this information.  Each line has 2 fields.

The first field is the name of a node.  Again, it is one character.
The second field is the estimated distance from the node named in the first field to the goal.
As an example consider the graph in the file: graph.txt

S A 3.0 <br />
S D 4.0 <br />
A B 4.0 <br />
B C 4.0 <br />
A D 5.0 <br />
B E 5.0 <br />
D E 2.0 <br />
F E 4.0 <br />
G F 3.0 <br />
`##### <br />
S 11.0 <br />
A 10.4 <br />
D 8.9 <br />
B 6.7 <br />
E 6.9 <br />
C 4.0 <br />
F 3.0 <br />
