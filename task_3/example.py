from get_random_graph import create_client_map_graph, find_least_central_node
from dijkstra import print_shortest_paths_from_node


def main():
    G = create_client_map_graph()
    start_node = find_least_central_node(G)
    print(f"Пошук найкоротших шляхів з вершини {start_node}")
    print_shortest_paths_from_node(G, start_node)


if __name__ == '__main__':
    main()
