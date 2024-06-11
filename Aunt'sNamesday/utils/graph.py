import os
import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(guests, dislikes, example_number, output_dir='output'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    G = nx.Graph()
    G.add_nodes_from(guests)
    G.add_edges_from(dislikes)

    pos = nx.spring_layout(G)
    colors = ['lightblue' if node in guests else 'lightgreen' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=3000, font_size=15, font_weight='bold')


    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

    output_path = os.path.join(output_dir, f'example{example_number}.png')
    plt.savefig(output_path)
    plt.close()
    return output_path
