# Causal_GE
This is the official repository associated to the paper ***Deregulation cascades in carcinogenesis***

Carcinogenesis is one example of transition between two biological states involving strong gene expression rearrangements. Normal and tumor states are understood as two different states of a Gene Regulatory Network.  In terms of the normal state characteristics, the transition may be thought as a deregulation process. According to a very abstract model for the transition, the available data on cancer risk support the idea of a single big jump in expression space, which may be associated to a deregulation cascade. Here, we use the measured frequency distribution of gene deregulations, and concepts from the probabilistic theory of causation in order to infer causal relations between pairs of genes and construct a deregulation causal network. Then, the deregulated genes in each sample are organized according to the network in such a way that they show the deregulation cascade behind the transition from the normal to the tumor state. The explicit analysis for prostate adenocarcinoma is given. In most cases, the cascade happens to be unique and initiated by a single deregulation event. Using results from a companion paper, we show that cascades conform classes which may be labeled by the deregulations in a predefined panel of 15 genes. The results of the paper may be checked in experiments with cellular lines or in animal models, and could have an impact on personalized cancer therapy .

The paper is based on the construction of the causal network described by J.P. Gomez in his Diploma Thesis and the construction of perfect panels of genes for cancer outlined in https://www.biorxiv.org/content/10.1101/2022.07.25.501449v2.  

# To-Do
- [X] Test generate brownian sample
- [X] Add GE notebook
- [X] Add initial genes to Figure 3 and a larger font
- [x] Manual draw normal concept graph
- [X] Make a table with pop, foxa1, and idh1 markers 
- [X] Make text for code data availability
- [X] Search for PTP genes in cluster 2
- [X] Check dysregulated genes or nodes in the minimal cancer sample
- [X] Create generate Brownian sample script
- [X] Eliminar Childless_frequencies.pdf
- [X] Eliminar Dysregulated_genes.pdf
- [X] Renombrar fig2. En el eje y contar nodos
- [X] Eliminar indgr_freq.pdf
- [X] Eliminar frequency_clusters.pdf
- [X] Renombrar fig3. Anadir un panel con la dependencia causal
- [X] Ver como hariamos la fig4 
- [X] Hacer seccion Tables y poner ahi las 4 tablas supplementarias
  - [X] Tabla I
  - [X] Tabla II
  - [X] Tabla III
  - [X] Tabla IV
- [X] Add otdegree brownians to samle table
- [X] Larger fig4 labels and change yticks
- [X] Do table names switch and push

  
# Repository sections
### Data
This folder includes all data files that are not generated as a result of our analyses, including the graph file and files to map between nodes and
gene names/ESEMBL ids

### result_files
Folder to allocate all files resulting from our analysis, excluding charts.

### Charts
Contains every generated figure included in the paper

### pyfuncs
Python utility functions

### Supplementary Materials
Tables included as supplementary materials in the paper (May be redundtant with others files in Data and result_files)
