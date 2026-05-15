import json
import pandas as pd

humic_skills_path = "humic_esco_matched_skills.csv"
job_data_path = "mapped_skills_with_occupations_and_skills.json"
output_path = "humic_skills_with_job_cooccurrences.csv"

humic_skills_df = pd.read_csv(humic_skills_path)

humic_skills_map = {
    row["ESCO Preferred Label"].lower(): row["Humic Skill"]
    for _, row in humic_skills_df
    .dropna(subset=["ESCO Preferred Label"])
    .iterrows()
}

with open(job_data_path, "r", encoding="utf-8") as file:
    job_data = json.load(file)

structured_results = []

for job in job_data:
    job_id = job.get("id")

    for item in job.get("items", []):
        job_skills = [
            {
                "skill_id": skill.get("skill", ""),
                "preferred_label": skill.get("skill_label_from_mapping", ""),
                "alternative_labels": skill.get("alternative_labels", [])
            }
            for skill in item.get("mapped_skills", [])
        ]

        for skill in job_skills:
            preferred_label = skill["preferred_label"].lower()

            if preferred_label in humic_skills_map:
                co_occurring_skills = [
                    {
                        "Skill ID": co_skill["skill_id"],
                        "Preferred Label": co_skill["preferred_label"],
                        "Alternative Labels": ", ".join(co_skill["alternative_labels"])
                    }
                    for co_skill in job_skills
                    if co_skill["preferred_label"].lower() != preferred_label
                ]

                structured_results.append({
                    "Job ID": job_id,
                    "Detected Humic Skill": humic_skills_map[preferred_label],
                    "Humic Preferred Label": skill["preferred_label"],
                    "Humic Alternative Labels": ", ".join(skill["alternative_labels"]),
                    "Co-occurring Skills": co_occurring_skills
                })

structured_df = pd.DataFrame(structured_results)
structured_df.to_csv(output_path, index=False)
