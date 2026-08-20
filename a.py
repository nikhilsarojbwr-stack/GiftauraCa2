import requests
from pprint import pprint

USER_AGENT = "NovelApp/1.0 (contact@example.com)"


def get_book_all_data(title):
    # 1. Search for the book
    search_url = "https://openlibrary.org/search.json"
    params = {
        "title": title,
        "limit": 1,  # get the best match
        "fields": "key"  # we only need the work key
    }
    resp = requests.get(search_url, params=params, headers={"User-Agent": USER_AGENT})
    resp.raise_for_status()
    docs = resp.json().get("docs", [])
    if not docs:
        return None

    work_key = docs[0]["key"]  # e.g., "/works/OL123456W"
    print(f"Found work key: {work_key}")

    # 2. Get full Work details
    work_url = f"https://openlibrary.org{work_key}.json"
    work_resp = requests.get(work_url, headers={"User-Agent": USER_AGENT})
    work_resp.raise_for_status()
    work_data = work_resp.json()

    # 3. Get all Editions for this Work
    editions_url = f"https://openlibrary.org{work_key}/editions.json"
    editions_resp = requests.get(editions_url, headers={"User-Agent": USER_AGENT})
    editions_resp.raise_for_status()
    editions_data = editions_resp.json()

    # 4. Combine everything
    result = {
        "work": work_data,
        "editions": editions_data.get("entries", [])
    }

    # Optionally, fetch Author details for each author key
    authors = []
    for author_ref in work_data.get("authors", []):
        author_key = author_ref.get("author", {}).get("key")
        if author_key:
            author_url = f"https://openlibrary.org{author_key}.json"
            author_resp = requests.get(author_url, headers={"User-Agent": USER_AGENT})
            if author_resp.status_code == 200:
                authors.append(author_resp.json())
    result["authors_details"] = authors

    return result


if __name__ == "__main__":
    data = get_book_all_data("Haunting Adeline")
    if data:
        # Pretty print the full result (but it's huge; you might want to save to file)
        print("\n=== WORK DATA ===")
        pprint(data["work"])

        print("\n=== EDITIONS ===")
        pprint(data["editions"])

        print("\n=== AUTHORS DETAILS ===")
        pprint(data["authors_details"])
    else:
        print("Book not found.")