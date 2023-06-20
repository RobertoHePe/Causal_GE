from pyfuncs.utils import generate_brownian_sample
import numpy as np
import networkx as nx


if __name__ == "__main__":
    # Load samples
    sample = np.abs(np.loadtxt("Data/sample.txt")).T
    # Load graph
    Graph = nx.read_adjlist(
        "Data/gene_network.adjlist", create_using=nx.DiGraph, nodetype=int
    )
    generate_brownian_sample(sample=sample, Graph=Graph)
