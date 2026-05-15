# Source Code

This folder contains the main Python scripts used in the HUMANE-SE thesis project.

## Scripts

### `data_collection.py`

Retrieves Software Engineering job postings from the SKILLAB Tracker API.

### `humics_esco_matching.py`

Performs semantic similarity matching between a curated humics skill list and ESCO skills using Sentence Transformers.

### `map_skills.py`

Maps extracted skill identifiers from job postings to readable skill labels through the SKILLAB skills API.

### `map_skills_and_occupations.py`

Maps both skill and occupation identifiers to human-readable labels.

### `map_skills_for_education_policies.py`

Creates enriched skill mappings intended for education policy and learning pathway analysis.

### `extract_humic_cooccurrences.py`

Identifies humics-related skills in job postings and extracts their co-occurring technical and soft skills.

### `communication_ego_network.py`

Builds and visualizes an ego network centered on the `communication` humics skill.

## Notes

The original dataset used in the thesis consisted of approximately 15,000 Software Engineering job postings collected between 2020 and 2024.

Large raw datasets and API outputs are not included in this repository.
