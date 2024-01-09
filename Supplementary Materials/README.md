# Paper supplementary materials
1. **Table I**: Characterization of network nodes. Includes
   - **Node**: Node index in adjacency list
   - **Frequency**: Node frequency among all samples  
   - **Frequency_in_cancer**: Node frequency among cancer samples
   - **Frequency_in_normal**: Node frequency among normal samples
   - **In_Degree**: Node in-degree
   - **Out_Degree**: Node out-degree
   - **Multiplicity**: Number of genes compressed in the node
   - **Associated_genes**: Names of genes compressed in the node

2. **Table II**: Causal Network inferred for PRAD. Stored as adjacency list as saved
   by NetworkX Python library

3. **Table III**: Characterization of samples
   - **Sample Index**: Index of the sample in Table IV
   - **TCGA ID**: Sample ID reported in the TCGA data
   - **Sample Type**: Sample classification as Normal or Tumor
   - **Total Deregulations**: Number of deregulated nodes
   - **Brownian Deregulations**: Number of Brownian deregulations
   - **Brownian Nodes (Out degree>0)**: Deregulated Brownian nodes with possitive out degree
   - **Cluster**: Associated cluster
   - **Other columns**: Deregulation state for the 15 genes included in the normal panel: *CFAP65,CDKN1C,AC245100.2,AC008764.8,LRATD2,AL137186.2,TRIM2,AL022332.1,MADCAM1,U3,AC012213.3,ENSG00000264976,OAT,AC007000.2,DNPH1*
  
4. **Table IV**: Discretized values of expression data for PRAD. Rows represent nodes and columns of the samples.
