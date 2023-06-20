import networkx as nx
import numpy as np
from tqdm import tqdm

def generate_brownian_sample(sample, Graph):
    brownian_sample = []
    transpGraph = Graph.reverse()
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