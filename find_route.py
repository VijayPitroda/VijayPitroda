# Importing modules
import sys
from queue import PriorityQueue
from heapq import heappush, heappop

# function for creating a graph from the input file containing data
def create_graph(filename):
	graph = {}
	file = open(filename, 'r')
	for line in file:
		if 'END OF INPUT' in line:
			return graph
		
		node_A, node_B, d = line.split()
		graph.setdefault(node_A, []).append((node_B, d))
		graph.setdefault(node_B, []).append((node_A, d))

# Uniformed cost search algorithm using Priority Queue as the data structure for evaluating and expanding the nodes
def ucs(graph, source, destination):
	visited = set()
	path = []
	queue = PriorityQueue()
	queue.put((0, [source]))

	while queue:
		# if no path is present beteween two nodes 	
		if queue.empty():
			print('distance: infinity\nroute: \nnone')
			return
		cost, path = queue.get()
		node = path[len(path)-1]
		if node not in visited:
			visited.add(node)
			if node == destination:
				path.append(cost)
				return path
			
			for n in neighbors(graph, node):
				if n not in visited:
					t_cost = cost + int(find_cost(graph, node, n))
					temp = path[:]
					temp.append(n)
					queue.put((t_cost, temp))

# function for finding neighbors in the graph
def neighbors(graph, node):
	points = graph[node]
	return [n[0] for n in points]

# function to calculate the cost of path beteween two nodes
def find_cost(graph, node_A, node_B):
	location = [n[0] for n in graph[node_A]].index(node_B)
	return graph[node_A][location][1]

# output the result of search
def display_path(graph, path):
	distance = path[-1]
	print('distance: '+ str(distance) + ' km')
	print('route: ')
	for p in path[:-2]:
		q = path.index(p)
		location = [r[0] for r in graph[p]].index(path[q+1])
		cost = graph[p][location][1]
		print(p + ' to ' + path[q+1] + ', ' + cost + ' km')

# defining the main function with all the arguments
def main():
	filename = sys.argv[1]
	source = sys.argv[2]
	destination = sys.argv[3]

	graph = {}
	graph = create_graph(filename)
		
	if source not in graph.keys():
		print('Source city not found')
		sys.exit()
	
	if destination not in graph.keys():
		print('Destination city not found')
		sys.exit()

	path = []
	path = ucs(graph, source, destination)

	if path:
		display_path(graph, path)

# calling for the execution of the main function
if __name__ == '__main__':
	main()	
