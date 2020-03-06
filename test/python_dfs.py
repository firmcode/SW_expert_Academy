#python dfs example

from queue import Queue

def dfs(graph, start_node):
	visit = list()
	stack = list()

	stack.append(start_node)

	while stack:
		node = stack.pop()
		if node not in visit:
			visit.append(node)
			stack.extend(graph[node])

	return visit


def bfs(graph, start_node):
	visit = {}
	q = Queue()

	q.put(start_node)

	while q.qsize() > 0:
		node = q.get()
		if node not in visit:
			visit[node]=True
			for nextNode in graph[node]:
				q.put(nextNode)

	return visit



if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))

