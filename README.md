# Causal_GE
This is the official repository associated to the paper ***Reanalyzing gene-expression data from a causal perspective***

Differential expression and co-expression analysis, pathway analysis, and dimensional reduction techniques are usual ways of processing gene expression data. As a result, we obtain sets of differentially expressed genes and enriched pathways, which are assumed to underly the main biological processes in the system under study.  In the present paper, we revisit gene-expression data by looking at it from a causal perspective. In particular, we examine TCGA gene expression data for prostate adenocarcinoma (PRAD). 

The paper is based on the construction of the causal network described by J.P. Gomez in his Diploma Thesis and the construction of perfect panels of genes for cancer outlined in https://www.biorxiv.org/content/10.1101/2022.07.25.501449v2.  

# To-Do
- [X] Test generate brownian sample
- [X] Add GE notebook
- [X] Add initial genes to Figure 3 and a larger font
- [x] Manual draw normal concept graph
- [ ] Make a table with pop, foxa1, and idh1 markers 
- [X] Make text for code data availability
- [ ] Search for PTP genes in cluster 2
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
- [ ] Add otdegree brownians to samle table
- [ ] Try desicion trees on clusters

  
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
