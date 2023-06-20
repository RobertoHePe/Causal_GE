import networkx as nx
import numpy as np
from tqdm import tqdm


def load_nodes_map(filename):
    """
    Loads a map to decompress nodes with multile genes

    Params:
    -------
    filename : string
        Path to map file

    Returns:
    --------
    nodes_map : dict
        Each key represent a compressed node and genes are its values
    """
    with open(filename) as reader:
        data = reader.readlines()

    nodes_map = {}

    for n, line in enumerate(data):
        nodes = line.split(" ")[:-1]
        nodes = [int(node) for node in nodes]
        nodes_map[n] = nodes

    return nodes_map


def load_genes_map(filename):
    """
    Loads a map to get gene alias from gene number

    Params:
    -------
    filename : string
        Path to map file

    Returns:
    --------
    nodes_map : dict
        Each key represent a gene number and gene alias is its value
    """
    with open(filename) as reader:
        data = reader.readlines()

    genes_map = {}

    for n, line in enumerate(data):
        gene = line[:-1]
        genes_map[n] = gene

    return genes_map


def generate_brownian_sample(sample, Graph):
    brownian_sample = []
    for i in tqdm(range(sample.shape[0])):
        br_sample = np.zeros_like(sample[i, :])
        alterd_genes = np.where(sample[i, :] == 1)[0]
        for gene in alterd_genes:
            parents = list(nx.descendants_at_distance(transpGraph, gene, 1))
            if sample[i, parents].sum() > 0:
                #print(sample[i, parents].sum())
                continue
            else:
                br_sample[gene] = 1
        brownian_sample.append(br_sample)
    brownian_sample = np.array(brownian_sample)
    return(brownian_sample)

if __name__ == "__main__":
    pass
