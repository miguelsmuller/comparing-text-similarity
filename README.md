# Text Similarity Comparison Project

## Overview

This Python project demonstrates the comparison of text similarity using two different methods: Sentence Transformers for semantic similarity and Fuzzy for character-based similarity. Text similarity measurement plays a significant role in various applications, and understanding the differences between these methods is crucial for making informed decisions.

For a more in-depth exploration of this comparison, including detailed insights and examples, I have written an article ["Comparing Text Similarity Measurement Methods: Sentence Transformers vs. Fuzzy"](https://dev.to/miguelsmuller/comparing-text-similarity-measurement-methods-sentence-transformers-vs-fuzzy-og3) available at dev.to.


## Project Structure

The project consists of the following components:

- `main.py`: Python script demonstrating the usage of both Sentence Transformers and Fuzzy.
- `requirements.txt`: List of required Python libraries for the project.

## Installation

Before running the project, make sure to install the required libraries. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `main.py` script to compare text similarity using Sentence Transformers and Fuzzy.

```bash
python app "João Matos da Silva" "João Pedro da Silva"
# Sentence Transformers:  0.8613903522491455
# Sentence Transformers:  0.79
```

```bash
python app "O vasto oceano é belo" "O imenso mar é deslumbrante."
# Sentence Transformers:  0.6285576224327087
# Sentence Transformers:  0.45
```

```bash
python app "The vast ocean is beautiful" "The immense sea is stunning"
# Sentence Transformers:  0.8006699085235596
# Sentence Transformers:  0.52
```

```bash
python app "color" "colour"
# Sentence Transformers:  0.973908543586731
# Sentence Transformers:  0.91
```

```bash
python app "The quick brown fox jumps over the lazy dog" "A fast brown fox leaps over a dozing dog"
# Sentence Transformers:  0.8295611143112183
# Sentence Transformers:  0.63
```

```bash
python app "John Smith" "Jon Smithe"
# Sentence Transformers:  0.7414223551750183
# Sentence Transformers:  0.9
```

2. Review the output to see the similarity scores for different text pairs.


