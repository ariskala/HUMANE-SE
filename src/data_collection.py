import requests
import json

base_url = "http://skillab-tracker.csd.auth.gr/api/jobs"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "sources": "kariera.gr"
}

max_pages = 10

all_results = []

for page in range(1, max_pages + 1):
    print(f"Fetching data from page {page}...")

    response = requests.post(
        f"{base_url}?page={page}",
        headers=headers,
        data=data
    )

    if response.status_code == 200:
        try:
            results = response.json()

            print(f"Data for page {page}:")
            print(
                json.dumps(
                    results,
                    indent=4,
                    ensure_ascii=False
                )
            )

            all_results.append(results)

        except ValueError as error:
            print(
                f"Error parsing JSON response "
                f"for page {page}: {error}"
            )
            break

    else:
        print(f"Error on page {page}: {response.status_code}")
        print(response.text)
        break

output_file = "api_response_jobs.json"

with open(
    output_file,
    mode="w",
    encoding="utf-8"
) as json_file:
    json.dump(
        all_results,
        json_file,
        indent=4,
        ensure_ascii=False
    )

print(
    f"All pages successfully saved "
    f"to '{output_file}'."
)
