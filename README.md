# Causal_GE
This is the official repository associated to the paper **Reanalyzing gene-expression data from a causal perspective**

Differential expression and co-expression analysis, pathway analysis, and dimensional reduction techniques are usual ways of processing gene expression data.
As a result, we obtain sets of differentially expressed genes and enriched pathways, which are assumed to underly the main biological processes in the system under study.  
In the present paper, we revisit gene-expression data by looking at it from a causal perspective.  

# To-Do
- [ ] Test generate brownian sample
- [X] Add GE notebook
- [ ] Add initial genes to Figure 3 and a larger font
- [ ] Manual draw normal concept graph
- [ ] Make a table with pop, foxa1, and idh1 markers 
- [ ] Make text for code data availability
- [ ] Search for PTP genes in cluster 2
- [ ] Add sample ID to samples in tables
- [ ] Table of dysregulated genes (isn't this the sample table?)
- [ ] Check dysregulated genes or nodes in the minimal cancer sample
- [ ] Create generate Brownian sample script
  
# Repository sections
### Data
This folder includes all data files that are not generated as a result of our analyses, including the graph file and files to map between nodes and
gene names/ESEMBL ids

### result_files
Folder to allocate all files resulting from our analysis, excluding charts.

### Charts
Contains every generated figure 

### pyfuncs
Utility functions
