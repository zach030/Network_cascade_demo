import matplotlib.animation as animation
import matplotlib.pyplot as plt

from random_walk import *


def update(num):
    ax.clear()

    # Background nodes
    null_nodes = nx.draw_networkx_nodes(G, pos=pos, nodelist=set(G.nodes()), node_color="white", ax=ax)
    null_nodes.set_edgecolor("black")
    nx.draw_networkx_edges(G, pos=pos, ax=ax, edge_color="gray")

    nx.draw_networkx_labels(G, pos=pos, font_color="black", ax=ax)
    nx.draw_networkx_nodes(G, pos=pos, nodelist=[seed], node_color='red', ax=ax)

    for step_i in range(1, num):
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i - 1]], node_color='lightcoral', ax=ax)
        nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[step_i]], node_color='red', ax=ax)
        nx.draw_networkx_edges(G, pos=pos, edgelist=[(path[step_i - 1], path[step_i])], width=2., ax=ax)

        # Scale plot ax
        ax.set_title("Frame %d" % step_i, fontweight="bold")
        ax.set_xticks([])
        ax.set_yticks([])

    nx.draw_networkx_nodes(G, pos=pos, nodelist=[path[0]], node_color='blue', ax=ax)
    plt.axis('off')


fig, ax = plt.subplots(figsize=(8, 6))
plt.axis('off')


def AnimateRandomWalk():
    # Build plot
    ani = animation.FuncAnimation(fig, update, frames=len(path), interval=1000, repeat=True)
    plt.show()
