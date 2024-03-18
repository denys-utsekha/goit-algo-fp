import heapq

import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
G.add_edge("Alice", "Bob", weight=5)
G.add_edge("Bob", "Charlie", weight=3)
G.add_edge("Charlie", "Diana", weight=4)
G.add_edge("Diana", "Eva", weight=2)
G.add_edge("Eva", "Alice", weight=6)
G.add_edge("Bob", "Diana", weight=5)
G.add_edge("Diana", "Alice", weight=1)


def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


shortest_paths = dijkstra(G, "Alice")
print(shortest_paths)


pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
