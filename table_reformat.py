import networkx as nx
import pandas as pd
import numpy as np

if __name__ == "__main__":
    # Load samples
    sample = np.abs(np.loadtxt("Data/sample.txt", dtype=int)).T
    pd.DataFrame(sample).to_csv('Supplementary Materials/Table IV.csv.gz', index=False)

    # Load graph
    Graph = nx.read_adjlist(
        "Data/gene_network.adjlist", create_using=nx.DiGraph, nodetype=int
    )
    nx.write_adjlist(Graph, 'Supplementary Materials/Table II.csv.gz', delimiter=',')


