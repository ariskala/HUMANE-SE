# HUMANE-SE Methodology

## Overview

HUMANE-SE is a semi-automated, data-driven framework designed to identify and analyze human-centric skills ("humics") in Software Engineering job markets.

The framework combines labor market intelligence, NLP-based skill extraction, semantic similarity analysis, and graph-based modeling to detect hybrid skill profiles and generate future-oriented learning recommendations.

---

## Methodological Pipeline

The HUMANE-SE framework consists of four primary stages:

1. Data Collection
2. Skill Extraction
3. Data Analysis
4. Humics Suggestion

---

## 1. Data Collection

The data collection stage focuses on retrieving Software Engineering job postings from labor market platforms.

### Data Source

- SKILLAB Tracker platform
- Kariera.gr and affiliated European job portals
- ISCO-08 Software Engineering occupation categories

### Dataset Characteristics

- Approximately 15,000 job postings
- Time period: 2020–2024
- Fields:
  - Job title
  - Job description
  - Experience level
  - Employment type
  - Location

### Objective

Build a large unstructured corpus of Software Engineering labor market data for downstream analysis.

---

## 2. Skill Extraction

The skill extraction stage identifies technical and human-centric skills from job descriptions.

### Technologies Used

- ESCO taxonomy
- ESCOX Skill Extractor
- Transformer-based NLP models
- Semantic similarity matching

### Process

1. Parse job descriptions
2. Detect skill mentions
3. Match skills to ESCO entities
4. Identify humics-related skills using semantic similarity

### Humics Lexicon

A curated humics lexicon was used to identify uniquely human skills such as:

- Communication
- Adaptability
- Empathy
- Collaboration
- Critical thinking
- Problem-solving

---

## 3. Data Analysis

The extracted skills were analyzed using graph-based network analysis techniques.

### Analysis Components

- Skill frequency analysis
- Co-occurrence matrix generation
- Network graph construction
- Degree centrality analysis
- Humics Hub identification

### Technologies

- Python
- NetworkX
- Plotly
- Graph visualization techniques

### Humics Hubs

Humics Hubs represent clusters of co-occurring technical and human-centric skills identified within Software Engineering job postings.

---

## 4. Humics Suggestion

The final stage transforms analytical findings into actionable recommendations.

### Recommendation Categories

- Hybrid Software Engineering job roles
- Human-centric learning pathways
- Future-oriented skill combinations

### AI-assisted Workflow

LLM-assisted prompting techniques were used to generate draft recommendations, followed by human-in-the-loop validation and refinement.

---

## Research Contribution

HUMANE-SE contributes to the intersection of:

- Software Engineering
- Artificial Intelligence
- Human-centric Computing
- Labor Market Analytics
- Skill Intelligence

The framework demonstrates how human-centric skills remain essential in increasingly AI-driven Software Engineering environments.
