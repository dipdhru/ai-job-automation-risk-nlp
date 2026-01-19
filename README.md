# AI Automation Risk Analysis of Job Roles using NLP

## Overview
This project uses Natural Language Processing (NLP) to analyze job descriptions
and assess the relative exposure of different job roles to AI-driven automation.
The goal is not to predict job loss, but to identify task and skill patterns
associated with higher or lower automation susceptibility.

## Problem Statement
With rapid advances in AI, certain job tasks are more likely to be automated
than others. This project analyzes real-world job descriptions to understand
which roles contain patterns that align with current AI capabilities.

## Dataset
- Job descriptions collected from O*NET database using Kaggle platform (https://www.kaggle.com/datasets/emarkhauser/onet-29-0-database/data) 
- Unstructured text data including role descriptions, responsibilities, and skills

## Methodology
- Text cleaning and preprocessing
- Tokenization and keyword extraction
- NLP-based analysis of job roles
- Aggregation of automation-related signals
- Comparative analysis across roles

## Key Insights
- Roles with repetitive, rule-based tasks show higher automation exposure
- Jobs emphasizing creativity, strategy, and human interaction show lower exposure
- Automation risk varies significantly within the same job title

## Technologies Used
- Python
- NLP (NLTK / spaCy / sklearn)
- Pandas, NumPy
- Matplotlib / Seaborn
- Streamlit

## Disclaimer
This project assesses **relative automation exposure** based on textual patterns
and does not predict job elimination or future labor market outcomes.

## Author
Dipanshu Singh

