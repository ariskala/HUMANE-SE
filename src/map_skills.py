import json
import requests

input_file_path = "api_response_jobs.json"
output_file_path = "mapped_skills_with_details.json"

skills_api_url = "http://skillab-tracker.csd.auth.gr/api/skills?page=1"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

print("Loading job posting data...")

with open(input_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

if not isinstance(data, list):
    raise ValueError(f"Expected input data to be a list, but got {type(data)}.")

skills_list = []

print("Extracting skills from job postings...")

for entry in data:
    for item in entry.get("items", []):
        skills_list.extend(item.get("skills", []))

print(f"Extracted {len(skills_list)} skills including duplicates.")

unique_skills = list(set(skills_list))

print(f"Identified {len(unique_skills)} unique skills.")

skill_mappings = {}

print("Mapping unique skills through the SKILLAB skills API...")

for index, skill in enumerate(unique_skills, start=1):
    print(f"Processing skill {index}/{len(unique_skills)}: {skill}")

    payload = {
        "ids": skill
    }

    try:
        response = requests.post(
            skills_api_url,
            headers=headers,
            data=payload
        )
        response.raise_for_status()

        response_data = response.json()
        items_data = response_data.get("items", [{}])[0]

        skill_mappings[skill] = {
            "skill_label_from_mapping": items_data.get("label", "Unknown"),
            "alternative_labels": items_data.get("alternative_labels", [])
        }

    except requests.exceptions.RequestException as error:
        print(f"Error occurred while mapping skill '{skill}': {error}")

        skill_mappings[skill] = {
            "skill_label_from_mapping": "Error",
            "alternative_labels": []
        }

print("Adding mapped skill information to job postings...")

for entry in data:
    for item in entry.get("items", []):
        item["mapped_skills"] = []

        for skill in item.get("skills", []):
            mapped_info = skill_mappings.get(skill)

            if mapped_info:
                item["mapped_skills"].append({
                    "skill": skill,
                    "skill_label_from_mapping": mapped_info["skill_label_from_mapping"],
                    "alternative_labels": mapped_info["alternative_labels"]
                })

print("Saving enriched job posting data...")

with open(output_file_path, mode="w", encoding="utf-8") as output_file:
    json.dump(
        data,
        output_file,
        indent=4,
        ensure_ascii=False
    )

print(f"Enriched data successfully saved to '{output_file_path}'.")
