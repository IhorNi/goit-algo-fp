import heapq
from prettytable import PrettyTable


def single_source_dijkstra_path(G, source):
    def dijkstra_recursive(pq, distances, shortest_paths):
        if not pq:
            return
        current_distance, current_node = heapq.heappop(pq)
        for neighbor in G.neighbors(current_node):
            distance = G[current_node][neighbor]['weight']
            new_distance = current_distance + distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]
                dijkstra_recursive(pq, distances, shortest_paths)

    shortest_paths = {source: [source]}
    distances = {node: float('inf') for node in G.nodes}
    distances[source] = 0
    pq = []
    heapq.heappush(pq, (0, source))
    dijkstra_recursive(pq, distances, shortest_paths)
    return shortest_paths, distances


def print_shortest_paths_from_node(G, start_node):
    shortest_paths, shortest_path_lengths = single_source_dijkstra_path(G, start_node)

    table = PrettyTable()
    table.field_names = ["Кінцева вершина", "Найкоротший шлях", "Довжина шляху"]
    table.align["Найкоротший шлях"] = "l"

    for destination, path in shortest_paths.items():
        length = shortest_path_lengths[destination]
        table.add_row([destination, " -> ".join(path), length])

    print(table)
