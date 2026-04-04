## 📌 Overview

This project is the official implementation of:

> **Embedding Social Perception Dimensions in a Semantic Space: Toward a Quantitative Synthesis**  
> Xuanlong QIN, Tony TAM 
> Journal of Social Computing, 2025

Paper link: [link](https://www.sciopen.com/article/10.23919/JSC.2025.0010)

and paper

> **Computational Evidence for the Two-Dimensional Structure of Social Evaluation: Pandemic-Era Insights From Americans’ Perceptions of Chinese and Japanese on Twitter**  
> Xuanlong QIN, Tony TAM 
> Social Science Computer Review, 2025

**Primary Maintainer:** Xuanlong QIN

This repository contains the code, experiments, and instructions to reproduce the results presented in the papers.

Basically, this project involve two parts and one illustrative study
- Part 1: The method to embedd social perception in semantic space (The JSC paper)
- Part 2: The theoretical synthesis of three social evaluation models (The SSCR paper)
- Illustrative study: the application of the methodology framework.

Even though this project is divided by two papers, the whole logic is coherent. 

---

## 1. Preparation 
### 1.1 Paper Data
Seed words: All seed words of SCM, DPM and SD are in fold "/doc/seed_words"
- Agency/communion are from [Pietraszkiewicz et al.(2018)](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.2561) 
- Warmth/competence are from [Nicolas et al.(2020)](https://onlinelibrary.wiley.com/doi/10.1002/ejsp.2724)
- Potency/Evaluation ar from [Osgood et al. (1957)](https://psycnet.apa.org/record/1958-01561-000)
- Antonym files from [Mohammad et al.2008;2013](https://aclanthology.org/D08-1103/)
- Word Embedddings
  - Googlenews, Glove and fastText can be found online.
  - For convenious relicate work, I uploaded my file as well.

### 1.2 Illustrative study
The twibot22 dataset can be applied from their [twibot22-github](https://github.com/LuoUndergradXJTU/TwiBot-22). I will also provide a processed version in osf.

### 1.3 Output
- Contrasting pairs (In the folder "/doc/contrasting_pairs")
- Dimesnions of Contrastng Pairs in Word Embeddings

## 2. Replication
## 2.1 Methods
### Step 1: Selecting contrasting pairs by mce alrorithms
- Selecting constrasting pairs by MCE algorithms.
- file: `step1.py`
- Input: seed words
- Output: contrasting pairs

### Step 2: Constructing contrasting pairs by mce alrorithms
- Building dimensions in word embeddings.
- file: `step2.py`
- Input: contrasting pairs
- Output: ".npy file" for different embeddings.

### Step 3: Projection method
- file: `step3.py`
- Input: word pairs
- Output: 2-dimensional framework

### 2.2 Description
All content of JSC paper are in JSC folder.
All content of SSCR paper are in SSCR folder.
Illustrative study is in a distinguished folder.