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


def map_node_name(node, nodes_map, genes_map):
    return [genes_map[gen] for gen in nodes_map[node]]


def retrieve_family_nodes(gene_family, compressed_nodes_map, genes_map):
    # Find genes index
    gene_family_idx = [
        i for i in range(len(genes_map)) if genes_map[i].startswith(gene_family)
    ]
    # Find gene nodes
    gene_family_nodes = [
        [
            i
            for i in range(len(compressed_nodes_map))
            if gene in compressed_nodes_map[i]
        ][0]
        for gene in gene_family_idx
    ]

    return gene_family_nodes


if __name__ == "__main__":
    pass
