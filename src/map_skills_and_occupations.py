import json
import requests

input_file_path = "api_response_jobs.json"
output_file_path = "mapped_skills_with_occupations.json"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}


def fetch_label_from_api(url, items, item_type):
    item_mappings = {}

    print(f"Mapping {item_type}s through the SKILLAB API...")

    for index, item in enumerate(items, start=1):
        print(f"Processing {item_type} {index}/{len(items)}: {item}")

        payload = {
            "ids": item
        }

        try:
            response = requests.post(
                url,
                headers=headers,
                data=payload
            )
            response.raise_for_status()

            response_data = response.json()
            item_data = response_data.get("items", [{}])[0]

            item_mappings[item] = {
                "label": item_data.get("label", "Unknown")
            }

        except requests.exceptions.RequestException as error:
            print(f"Error occurred while mapping {item_type} '{item}': {error}")

            item_mappings[item] = {
                "label": "Error"
            }

    return item_mappings


print("Loading job posting data...")

with open(input_file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

if not isinstance(data, list):
    raise ValueError(f"Expected input data to be a list, but got {type(data)}.")

skills_list = []
occupations_list = []

print("Extracting skills and occupations from job postings...")

for entry in data:
    for item in entry.get("items", []):
        skills_list.extend(item.get("skills", []))
        occupations_list.extend(item.get("occupations", []))

print(
    f"Extracted {len(skills_list)} skills and "
    f"{len(occupations_list)} occupations including duplicates."
)

unique_skills = list(set(skills_list))
unique_occupations = list(set(occupations_list))

print(
    f"Identified {len(unique_skills)} unique skills and "
    f"{len(unique_occupations)} unique occupations."
)

skill_mappings = fetch_label_from_api(
    "http://skillab-tracker.csd.auth.gr/api/skills?page=1",
    unique_skills,
    "skill"
)

occupation_mappings = fetch_label_from_api(
    "http://skillab-tracker.csd.auth.gr/api/occupations?page=1",
    unique_occupations,
    "occupation"
)

print("Adding mapped skills and occupations to job postings...")

for entry in data:
    for item in entry.get("items", []):
        item["mapped_skills"] = []
        item["mapped_occupations"] = []

        for skill in item.get("skills", []):
            mapped_info = skill_mappings.get(skill)

            if mapped_info:
                item["mapped_skills"].append({
                    "skill": skill,
                    "skill_label": mapped_info["label"]
                })

        for occupation in item.get("occupations", []):
            mapped_info = occupation_mappings.get(occupation)

            if mapped_info:
                item["mapped_occupations"].append({
                    "occupation": occupation,
                    "occupation_label": mapped_info["label"]
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
