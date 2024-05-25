from faker import Faker
import networkx as nx
import random


def create_client_map_graph(n_places=10, n_connections=4):
    fake = Faker()
    places = [fake.unique.first_name() for _ in range(n_places)]
    G = nx.Graph()
    G.add_nodes_from(places)
    for place in places:
        connections = random.sample(places, random.randint(1, n_connections))
        for connected_place in connections:
            if connected_place != place:
                weight = random.randint(1, 10)
                G.add_edge(place, connected_place, weight=weight)
    return G


def find_least_central_node(G):
    degree_centrality = nx.degree_centrality(G)
    return min(degree_centrality, key=degree_centrality.get)
