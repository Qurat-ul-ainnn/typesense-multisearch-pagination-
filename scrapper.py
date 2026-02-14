"""
scraper.py

This script demonstrates how to:
- Send a Typesense multi_search request
- Handle pagination properly
- Collect all results
- Export results to CSV

This is a GENERIC example project for educational purposes.
No real API keys or proprietary services are included.
"""

import requests
import json
import math
import csv
import time
from config import BASE_URL, HEADERS, PER_PAGE


def get_total_results():
    """
    Makes an initial request to determine total number of results.
    We only request 1 item to minimize load.
    """

    payload = {
        "searches": [{
            "collection": "your_collection_name",
            "q": "*",
            "query_by": "title,description",
            "page": 1,
            "per_page": 1
        }]
    }

    response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
    response.raise_for_status()

    data = response.json()

    return data["results"][0]["found"]


def fetch_all_results():
    """
    Fetches all pages using pagination logic.
    """

    total = get_total_results()
    total_pages = math.ceil(total / PER_PAGE)

    print(f"Total results found: {total}")
    print(f"Total pages to fetch: {total_pages}")

    all_items = []

    for page in range(1, total_pages + 1):

        payload = {
            "searches": [{
                "collection": "your_collection_name",
                "q": "*",
                "query_by": "title,description",
                "page": page,
                "per_page": PER_PAGE
            }]
        }

        response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()

        data = response.json()
        hits = data["results"][0]["hits"]

        for hit in hits:
            all_items.append(hit["document"])

        print(f"Fetched page {page}/{total_pages}")
        time.sleep(0.2)  # Prevent rate limiting

    return all_items


def save_to_csv(data, filename="output.csv"):
    """
    Saves list of dictionaries to CSV file.
    """

    if not data:
        print("No data to save.")
        return

    fieldnames = sorted({key for item in data for key in item.keys()})

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Data saved to {filename}")


if __name__ == "__main__":
    results = fetch_all_results()
    save_to_csv(results)
