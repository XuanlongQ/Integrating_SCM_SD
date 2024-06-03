# Integrating_SCM_SD
This repository for replicate the paper "Big Two" Embeddings. 

The more details are as follow, 

## Data
Seed words: All seed words of SCM, DPM and SD are in fold "/doc/seed_words"
- agency/communion are from [Pietraszkiewicz et al.(2018)](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.2561) 
- warmth/competence are from [Nicolas et al.(2020)](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.2724)
- Potency/Evaaluation ar from [Osgood et al. (1957)](https://psycnet.apa.org/record/1958-01561-000)
- Antonym files from [Mohammad et al.2008;2013](https://aclanthology.org/D08-1103/)
- Word Embedddings
  - Googlenews, Glove and fastText can found online.
  - For convenious relicate work, I uploaded my file as well.


## Output
- 1. Contrasting pairs (In the folder "/doc/contrasting_pairs")
- 2. Dimesnions of Contrastng Pairs in Word Embeddings

## Methods
### Study 1.py: Selecting contrasting pairs by mce alrorithms

- Selecting constrasting pairs by MCE algorithms.
- file: study1.py
- Input: seed words
- Output: contrasting pairs

### Study 2.py: Constructing contrasting pairs by mce alrorithms

- Building dimensions in word embeddings.
- file: study2.py
- Input: contrasting pairs
- Output: ".npy file" for different embeddings.

## Drawing Pictures
### Fig3.Cosine Similarity Matrix of Social Perception Dimensions

- file: study11.py
- input: ".npy" file
- output: heatmap


### Fig4 and Fig 5. 

#### Fig 4. The Elbow Method for All Contrasting Pairs in 
#### Fig 5. The Visualization of Two-dimensional Reduction for All Contrasting Pairs 

- file: Study 5.py
- input: ".npy" files
- output: Clustering map

### Fig 6. The results of PCA dimension reductions and cosine similarity heatmap for all content dimensions across social perception models

- file: Study 4.py
- input: ".npy" files
- output: Heatmap and 2-dimensional Vectors


### Fig 8. Cosine Similarity Between Content Dimensions in SD, DPM, and SCM across Different Word Embeddings

- file: study 10.py
- input: ".npy" files
- output: heatmap


## Drawing tables
### Table 3. Top Five Seed Word Pairs for New Content Dimension

- file: study 8.py
- input: all contrasting pairs
- output: seed words with highest similarity

### Table 4. The Predicated Performance of Content Dimensions across Social Perception Models Using Personality Traits as Gold-standard Classification

We need to project 300-dimensional content dimensions to 2-dimensional space first
- files: study3.py, study6.py
- input: Contransting pairs, personality traits
- output: predicative performance

### Table 5. The predicted performance of content dimensions across social perception models which constructed by non-contrasting word pairs


We need to project 300-dimensional content dimensions to 2-dimensional space first
- file: study9.py, study3.py, and study6.py
- SCM: Using QT's computational stereotype content dictionaries
- DPM: Using study 9.py to generate seed words
- SD: Using study 9.py to generate seed words
- input: Non-contransting pairs, personality traits
- output: predicative performance